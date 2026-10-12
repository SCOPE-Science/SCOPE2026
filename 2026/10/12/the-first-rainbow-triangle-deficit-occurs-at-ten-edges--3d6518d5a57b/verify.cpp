// Exact finite checks for the colored triangle extremum; GNU C++17.
#include <bits/stdc++.h>
using namespace std;
static int rainbow(const vector<tuple<int,int,int>>& es){
    int c[6][6]; memset(c,-1,sizeof(c));
    for(auto [u,v,w]:es){if(c[u][v]!=-1) throw runtime_error("duplicate edge");c[u][v]=c[v][u]=w;}
    int t=0;
    for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)for(int k=j+1;k<6;k++) {
        int a=c[i][j],b=c[i][k],d=c[j][k];
        if(a>=0&&b>=0&&d>=0&&a!=b&&a!=d&&b!=d)t++;
    }
    return t;
}
int main(){
    unsigned long long profiles=0, contain_k5_10=0, contain_k5_11=0;
    unsigned long long strong10=0,strong11=0;
    int maxnon10=0,maxnon11=0;
    for(int n=3;n<=7;n++){
        vector<pair<int,int>> ed;int index[7][7];memset(index,-1,sizeof(index));
        for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){index[i][j]=index[j][i]=(int)ed.size();ed.emplace_back(i,j);}
        vector<unsigned long long> triangles,k5sets;
        for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++)
            triangles.push_back((1ULL<<index[i][j])|(1ULL<<index[i][k])|(1ULL<<index[j][k]));
        for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)for(int d=c+1;d<n;d++)for(int e=d+1;e<n;e++){
            int vv[5]={a,b,c,d,e};unsigned long long z=0;
            for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)z|=1ULL<<index[vv[i]][vv[j]];
            k5sets.push_back(z);
        }
        const unsigned long long end=1ULL<<ed.size();
        for(unsigned long long mask=0;mask<end;mask++){
            int m=__builtin_popcountll(mask);if(m!=10&&m!=11)continue;
            profiles++;
            int tri=0;for(auto z:triangles) if((mask&z)==z)tri++;
            bool k5=false;for(auto z:k5sets)if((mask&z)==z){k5=true;break;}
            if(m==10){maxnon10=max(maxnon10,k5?0:tri);if(tri>=8){strong10++;if(!k5) throw runtime_error("10 edges, 8+ triangles, no K5");contain_k5_10++;}}
            if(m==11){maxnon11=max(maxnon11,k5?0:tri);if(tri>=9){strong11++;if(!k5) throw runtime_error("11 edges, 9+ triangles, no K5");contain_k5_11++;}}
        }
    }
    cout<<"underlying_graph_profiles="<<profiles<<"; max_non_K5_t10="<<maxnon10<<"; max_non_K5_t11="<<maxnon11<<"; implication_profiles_10="<<strong10<<"; implication_profiles_11="<<strong11<<"\n";
    // Exhaust all 3^10 assignments of three colors on K5; check 7 is sharp.
    int pairs[5][5];memset(pairs,-1,sizeof(pairs));vector<pair<int,int>> ed;
    for(int i=0;i<5;i++)for(int j=i+1;j<5;j++){pairs[i][j]=pairs[j][i]=ed.size();ed.emplace_back(i,j);}
    vector<array<int,3>> tris;
    for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)for(int k=j+1;k<5;k++)tris.push_back({pairs[i][j],pairs[i][k],pairs[j][k]});
    int best=0,attain=0;for(int code=0;code<59049;code++){
        int cols[10],q=code;for(int i=0;i<10;i++){cols[i]=q%3;q/=3;}
        int cnt=0;for(auto x:tris) if(cols[x[0]]!=cols[x[1]]&&cols[x[0]]!=cols[x[2]]&&cols[x[1]]!=cols[x[2]])cnt++;
        if(cnt>best){best=cnt;attain=1;}else if(cnt==best)attain++;
    }
    if(best!=7)throw runtime_error("K5 rainbow upper failure");
    cout<<"K5_colorings=59049; K5_max_rainbow="<<best<<"; K5_max_colorings="<<attain<<"\n";
    const vector<tuple<int,int,int>> K4={{0,1,0},{0,2,1},{0,3,2},{1,2,2},{1,3,1},{2,3,0}};
    vector<vector<tuple<int,int,int>>> witness(12);
    witness[0]={};witness[1]={{0,1,0}};witness[2]={{0,1,0},{0,2,1}};
    witness[3]={{0,1,0},{0,2,1},{1,2,2}};
    witness[4]={{0,1,0},{0,2,1},{1,2,2},{0,3,2}};
    witness[5]=K4;witness[5].erase(witness[5].begin());
    witness[6]=K4;
    for(int m=7;m<=11;m++){
        witness[m]=K4;
        witness[m].push_back({4,0,2});
        if(m>=8)witness[m].push_back({4,1,1});
        if(m>=9)witness[m].push_back({4,2,0});
        if(m==10)witness[m].push_back({5,0,0});
        if(m==11){witness[m].push_back({5,0,1});witness[m].push_back({5,1,2});}
    }
    const int target[12]={0,0,0,1,1,2,4,4,5,7,7,8};
    for(int m=0;m<=11;m++){
        int t=rainbow(witness[m]);if((int)witness[m].size()!=m||t!=target[m]){
            cerr<<"FAIL witness m="<<m<<" got m="<<witness[m].size()<<" t="<<t<<"\n";return 1;
        }
        cout<<"m="<<m<<" R="<<t<<"\n";
    }
    cout<<"ALL CHECKS PASSED\n";
}
