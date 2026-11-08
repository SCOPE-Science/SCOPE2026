# Independent mathematical audit

## correctness

PASS

For recursive trees grown by independent uniform parents and n>=2, let L=leaf count and W=unordered-pair distance sum, A=sum of distance centralities of leaves. For a fixed size-m tree, adding a child at uniform parent P gives L’=L+1-J and W’=W+m+S(P), J=1_{P leaf}. The leaf-centrality update yields E(W_(m+1)-A_(m+1)|T_m)=W_m-A_m-(1-1/m)L_m. With E L_m=m/2 this telescopes to E(W_m-A_m)=-(m-1)(m-2)/4. Total covariance of L’,W’ gives C_(m+1)=(m+1)C_m/m-(m-1)(m-2)/(4m), C2=0; summing yields C_n=nH_n-(n²+5n-2)/4, 0 at n2/3 and strictly negative n>=4. Independently enumerated all recursive parent lists for n2..8 (5040 trees at n8) and computed W by BFS pair distances, confirming mean identity and exact covariance. The optional scaled-correlation constant follows from established Neininger 2002 Wiener variance (31-3π²)n^4/18 and Var L=n/12. Finite enumeration corroborates, the recurrence proves all n.

## originality

PASS

Neininger 2002 Theorem 1.2 treats the Wiener index jointly with INTERNAL PATH LENGTH, not leaf count; its full 11-page source was read through authorized institutional access. Grübel–Michailow 2014 treats Wiener asymptotics via boundary theory, not this mixed leaf centrality. The exact mixed covariance is not present in those examined claims.

## value

PASS

Leaf number and Wiener distance are two canonical structural statistics of a uniform recursive tree. Their exact mixed covariance and strict negative sign for all n>=4 are a natural previously undetermined dependency law; its -n²/4 scale differs from vanishing correlation and requires a leaf-centrality auxiliary observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
