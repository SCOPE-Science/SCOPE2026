// Exact finite verification for single length-2 tandem duplication codes.
// Compile: g++ -O3 -std=c++17 verify.cpp -o verify && ./verify
// Only standard C++ is needed apart from GCC's bitset set-bit iterators.
#include <bits/stdc++.h>
using namespace std;
using B = bitset<512>;
static B compatible[512];
static int best;
static unsigned long long explored;
static vector<int> path, witness;

// Proper greedy coloring of the induced compatibility graph.
// A clique can use at most one vertex of each color.
static void color_sort(B P, vector<int>& order, vector<int>& color) {
    int c=0;
    while (P.any()) {
        ++c;
        B uncolored_this_class=P;
        while (uncolored_this_class.any()) {
            int v=(int)uncolored_this_class._Find_first();
            order.push_back(v);
            color.push_back(c);
            P.reset(v);
            uncolored_this_class.reset(v);
            uncolored_this_class &= ~compatible[v];
        }
    }
}

// Exhaustive branch-and-bound maximum clique: the coloring bound prunes
// only branches that cannot improve the incumbent. This proves an upper
// bound as well as exhibiting an attaining independent set.
static void expand(B P) {
    ++explored;
    if (P.none()) {
        if ((int)path.size()>best) {
            best=(int)path.size(); witness=path;
        }
        return;
    }
    vector<int> order,color;
    color_sort(P,order,color);
    for (int i=(int)order.size()-1;i>=0;--i) {
        if ((int)path.size()+color[i]<=best) return;
        const int v=order[i];
        path.push_back(v);
        expand(P & compatible[v]);
        path.pop_back();
        P.reset(v);
    }
}
static void generate(int m,int t,vector<int>& cur,vector<vector<int>>& out) {
    if (m==1) {cur.push_back(t);out.push_back(cur);cur.pop_back();return;}
    for (int i=0;i<=t;i++) {cur.push_back(i);generate(m-1,t-i,cur,out);cur.pop_back();}
}
static vector<vector<int>> signatures(int m,int t) {
    vector<int> cur;vector<vector<int>> out;
    generate(m,t,cur,out);return out;
}
static pair<int,vector<vector<int>>> solve(int m,int t) {
    const auto V=signatures(m,t);
    const int N=(int)V.size();
    if (N>512) throw runtime_error("graph exceeds capacity");
    B P;
    for(int i=0;i<N;i++) {
        P.set(i); compatible[i].reset();
        for(int j=0;j<N;j++) if(i!=j) {
            int d=0;
            for(int k=0;k<m;k++) d+=abs(V[i][k]-V[j][k]);
            if(d!=2) compatible[i].set(j);
        }
    }
    best=0; explored=0;path.clear();witness.clear();
    expand(P);
    if ((int)witness.size()!=best) throw runtime_error("missing witness");
    // Check that the exhibited signatures never have distance two.
    for(int i=0;i<(int)witness.size();i++)
      for(int j=i+1;j<(int)witness.size();j++) {
        int d=0;
        for(int k=0;k<m;k++) d+=abs(V[witness[i]][k]-V[witness[j]][k]);
        if(d==2) throw runtime_error("invalid independent set");
      }
    vector<vector<int>> selected;
    for(int i:witness) selected.push_back(V[i]);
    return {best,selected};
}

static string construct(int prefix,int m,const vector<int>& residue,
                        const vector<int>& sig) {
    string deriv;
    for(int i=0;i<m;i++) {
        deriv.append(residue[i]+2*sig[i],'0');
        if(i+1<m) deriv+='1';
    }
    string x;
    x+=char('0'+(prefix>>1)); x+=char('0'+(prefix&1));
    for(char c:deriv) x+=char('0'+((c-'0')^(x[x.size()-2]-'0')));
    return x;
}
static vector<string> duplicates(const string& x) {
    vector<string> out;
    for(int i=0;i+2<=(int)x.size();i++)
        out.push_back(x.substr(0,i+2)+x.substr(i,2)+x.substr(i+2));
    sort(out.begin(),out.end());out.erase(unique(out.begin(),out.end()),out.end());
    return out;
}
static long long choose(int n,int k) {
    if(k<0||k>n)return 0;
    long long r=1;
    for(int i=1;i<=k;i++)r=r*(n-i+1)/i;
    return r;
}
int main() {
    // The input lengths 3,...,15 are all and only the asserted domain.
    const long long expected[]={0,0,0,8,16,28,48,84,148,260,460,816,
                                1440,2552,4568,8224};
    // The standalone alpha.csv accompanies this code. Every independent-set
    // value in that published table is checked against a newly solved graph.
    map<pair<int,int>,pair<int,int>> alpha_table;
    ifstream in("alpha.csv");
    if (!in) throw runtime_error("alpha.csv missing");
    string line;
    getline(in,line); // CSV header
    while (getline(in,line)) {
        if (line.empty()) continue;
        replace(line.begin(),line.end(),',',' ');
        istringstream fields(line);
        int m,t,vertices,independence;
        if (!(fields>>m>>t>>vertices>>independence))
            throw runtime_error("unreadable alpha.csv row");
        alpha_table[{m,t}]={vertices,independence};
    }
    if (alpha_table.size()!=56) throw runtime_error("wrong number of graph types");
    map<pair<int,int>,pair<int,vector<vector<int>>>> cache;
    const long long roots[]={0,0,0,8,16,28,48,80,132,216,352,572,928,1504,2436,3944};
    for(int n=3;n<=15;n++) {
        const int L=n-2;
        long long optimal=0, constructed=0, root_classes=0;
        set<string> output_words;
        for(int m=1;m<=L+1;m++) {
            for(int r=0;r<=m;r++) {
                int slack=L-(m-1)-r;
                if(slack<0||(slack%2))continue;
                int t=slack/2;
                auto key=make_pair(m,t);
                if(!cache.count(key))cache[key]=solve(m,t);
                if(!alpha_table.count(key) ||
                   (int)signatures(m,t).size()!=alpha_table.at(key).first ||
                   cache.at(key).first!=alpha_table.at(key).second)
                    throw runtime_error("alpha.csv disagrees with exhaustive search");
                const auto& selected=cache.at(key).second;
                const long long al=(long long)cache.at(key).first;
                if((long long)selected.size()!=al)throw runtime_error("alpha mismatch");
                optimal+=4*choose(m,r)*al;
                root_classes+=4*choose(m,r);
                // Construct every optimum codeword, not merely one sample
                // per type; independently test its direct error outputs.
                for(int mask=0;mask<(1<<m);mask++) {
                    if(__builtin_popcount((unsigned)mask)!=r)continue;
                    vector<int> rho(m);
                    for(int j=0;j<m;j++)rho[j]=(mask>>j)&1;
                    for(int prefix=0;prefix<4;prefix++)for(const auto& s:selected) {
                        string x=construct(prefix,m,rho,s);
                        if((int)x.size()!=n)throw runtime_error("bad word length");
                        constructed++;
                        for(const auto& y:duplicates(x))
                            if(!output_words.insert(y).second)
                                throw runtime_error("two selected inputs share a descendant");
                    }
                }
            }
        }
        if(optimal!=expected[n]||constructed!=optimal||root_classes!=roots[n])
            throw runtime_error("incorrect exact maximum or root benchmark");
        cout<<n<<','<<optimal<<','<<output_words.size()<<'\n';
    }
    cout<<"VERIFY_OK\n";
}
