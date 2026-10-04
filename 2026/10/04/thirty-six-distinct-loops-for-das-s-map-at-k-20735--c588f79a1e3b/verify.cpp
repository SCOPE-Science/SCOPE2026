#include <bits/stdc++.h>
using namespace std;

struct Data { int count; vector<vector<int>> cycles; };

int main(){
    const int KMAX = 20735;
    const int N = 2*KMAX + 2;
    vector<int> lpf(N+1,0);
    for(int p=2;p<=N;p++) if(lpf[p]==0){
        for(int m=p;m<=N;m+=p) lpf[m]=p;
    }
    vector<int> primes;
    for(int p=2;p<=KMAX;p++) if(lpf[p]==p) primes.push_back(p);

    auto enumerate_k = [&](int k, bool keep_cycles)->Data {
        int M=2*k+2;
        vector<int> assigned(M+1,0), mark(M+1,0), idx(M+1,-1);
        int run=0, cid=0;
        vector<vector<int>> cycles;
        for(int p:primes){
            if(p>k) break;
            if(assigned[p]) continue;
            ++run;
            vector<int> path;
            int x=p;
            while(true){
                if(x<2 || x>M){ cerr << "out-of-bound state" << endl; exit(2); }
                if(assigned[x]){
                    int c=assigned[x];
                    for(int y:path) assigned[y]=c;
                    break;
                }
                if(mark[x]==run){
                    int s=idx[x];
                    ++cid;
                    vector<int> cyc(path.begin()+s,path.end());
                    for(int j=s;j<(int)path.size();j++) assigned[path[j]]=cid;
                    for(int j=0;j<s;j++) assigned[path[j]]=cid;
                    if(keep_cycles){
                        int pos=min_element(cyc.begin(),cyc.end())-cyc.begin();
                        rotate(cyc.begin(),cyc.begin()+pos,cyc.end());
                        cycles.push_back(cyc);
                    }
                    break;
                }
                mark[x]=run;
                idx[x]=(int)path.size();
                path.push_back(x);
                x = (lpf[x]==x ? x+k : lpf[x]);
            }
        }
        if(keep_cycles){
            sort(cycles.begin(),cycles.end());
        }
        return {cid,cycles};
    };

    int best=0, first_best=-1;
    vector<pair<int,int>> records;
    for(int k=1;k<=KMAX;k+=2){
        int c=enumerate_k(k,false).count;
        if(c>best){ best=c; first_best=k; records.push_back({k,c}); }
        if(k<20735 && c>=36){ cerr << "earlier k with >=36 loops: "<<k<<"\n"; return 3; }
    }
    if(best!=36 || first_best!=20735){
        cerr << "unexpected final record " << best << " at " << first_best << "\n"; return 4;
    }
    auto d=enumerate_k(20735,true);
    if(d.count!=36 || d.cycles.size()!=36) return 5;
    map<int,int> hist;
    for(auto &c:d.cycles) hist[(int)c.size()]++;
    map<int,int> expected{{4,6},{6,14},{8,10},{10,5},{12,1}};
    if(hist!=expected){ cerr<<"length histogram mismatch\n"; return 6; }

    cout << "VERIFY_OK\n";
    cout << "ODD_RECORDS";
    for(auto [k,c]:records) cout << " " << k << ":" << c;
    cout << "\n";
    cout << "K20735_LOOP_COUNT " << d.count << "\n";
    cout << "LENGTH_HIST 4:6 6:14 8:10 10:5 12:1\n";
    for(size_t i=0;i<d.cycles.size();++i){
        cout << "CYCLE " << setw(2) << setfill('0') << (i+1);
        for(int x:d.cycles[i]) cout << " " << x;
        cout << "\n";
    }
}
