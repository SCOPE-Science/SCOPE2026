# Independent mathematical audit

## correctness

PASS

With 2<=m<=n, f:V(K_m box K_n)->{0,1,2,3,4} satisfies f(v)+sum_{u neighbor, f(u)>0}(f(u)-1)>=3 for f(v)<3, using open neighborhoods. Writing a_ij=max(f_ij-1,0), row r_i and column c_j surplus, B=sum r_i=sum c_j and T=#positive cells gives exact weight W=B+T. At labels 0,1,2 the necessary and sufficient row-column inequalities are r_i+c_j>=3, >=2, >=3, respectively (label 2 self surplus counted twice). If some column has c_j=0, every row incurs weight >=4, so W>=4m. Otherwise T>=n: if all rows r_i>=2 then W>=2m+n; if a row r_i=0 then every c_j>=2 and W>=3n; if some row r_i=1, writing a=#columns of surplus one, each such column needs two positive cells, so T>=n+a and B>=2n-a, hence W>=3n. The two explicit construction schemes yield 4m when n>=2m and 2m+n when m<=n<=2m. I independently enumerated all sub-bound assignments for six small boards (122,882,6075,49296,22330,272090 cases) with no counterexample; all-order proof is the surplus argument and the explicit construction, not these finite searches.

## originality

PASS

Triple Roman domination is the five-label defense invariant in Abdollahzadeh Ahangar et al. (2021/2024 manuscript), not Roman {3} domination nor strong/total Roman variants. The inspected foundational primary article gives the definition, general bounds and other families; no rook graph exact formula was seen. The generic degree bound yields only 12 at 5x5 while the new exact formula gives 15, proving that bound alone does not imply the result. Khalili et al 2023 closely related [k]-Roman primary was accessible only at abstract level (full text 403); this is a specific residual priority risk, not a scientific failure. Resultary’s Roman {3} complete-prism record is a different invariant and does not automatically cover triple Roman K_m box K_n.

## value

PASS

A complete two-parameter exact invariant for rook/line graphs of K_{m,n} with a genuine threshold at n=2m, new matching lower bound and constructive optimal defenses. Ordinary generic degree arguments leave a strict gap on balanced boards. Infinite natural product family and sharp phase transition are mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
