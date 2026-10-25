# Three-leader coherence on strictly rectangular rook graphs: a sharp two-row boundary

## Finding
Let \(G_{m,n}=K_m\square K_n\) be the unweighted rectangular rook graph, with integers \(2\le m<n\), and give its edges unit conductance. For any **three distinct noise-free leaders** \(S\subset V(G_{m,n})\), define the total follower coherence cost
\[
J_{m,n}(S)=\operatorname{tr}\big((L_{V\setminus S,V\setminus S})^{-1}\big),
\]
where \(L\) is the combinatorial graph Laplacian. Then **all** optimal three-leader sets and the exact minimum are as follows.

1. If \(m=2<n\), the leaders occupy **three distinct second coordinates**, with **two in one first-coordinate row and one in the other**. Exactly \(6\binom n3\) unordered triples attain the minimum
\[
J_{2,n}^{\min}=\frac{15n^4+16n^3-31n^2-58n-24}{n(n+1)(n+2)(5n+3)}.
\]
2. If \(3\le m<n\), the leaders have **pairwise distinct first coordinates and pairwise distinct second coordinates** (three nonattacking rooks). Exactly \(6\binom m3\binom n3\) unordered triples attain the minimum
\[
J_{m,n}^{\min}=\frac{2(2m^3n^3+4m^3n^2-m^3n-6m^3+4m^2n^3-2m^2n^2-12m^2n-mn^3-12mn^2-6n^3)}{3mn(m+n)(mn+m+n)}.
\]
The classifications are strict: no other triple attains the stated minimum. The transition from two available rows to three is a sharp combinatorial feasibility boundary, not an asymptotic approximation; equal-factor rook graphs are deliberately excluded.

## Assumptions and scope
Vertices are ordered pairs \((i,j)\in\{0,\dots,m-1\}\times\{0,\dots,n-1\}\). Distinct vertices are adjacent if they agree in exactly one coordinate. Edge conductances are exactly one, followers receive independent unit-variance disturbances, and the three leaders are fixed with no disturbances. The matrix trace used here is twice the usual steady-state variance of the unit-noise Ornstein–Uhlenbeck follower model, so no variance-normalization factor appears in the theorem. No claim is made for square rook graphs, weighted or directed variants, or more-than-three-leader variants.

## Proof
Write \(N=mn\), \(P_r=I_r-\mathbf1\mathbf1^\mathsf T/r\), and \(E_r=\mathbf1\mathbf1^\mathsf T/r\). The nonzero spectral projectors of the rook-graph Laplacian are \(P_m\otimes E_n\), \(E_m\otimes P_n\), and \(P_m\otimes P_n\), with eigenvalues \(m,n,m+n\), respectively. Thus its Moore–Penrose inverse \(H=L^+\) and its square satisfy, for \(p=1,2\),
\[
H^p=\frac{P_m\otimes E_n}{m^p}+\frac{E_m\otimes P_n}{n^p}+\frac{P_m\otimes P_n}{(m+n)^p}.
\]
Set \(S=\{a,b,c\}\) and \(U=\{b,c\}\). The grounded Green matrix when only \(a\) is grounded has entries
\[
G_a(u,v)=H_{uv}-H_{ua}-H_{av}+H_{aa}.
\]
Grounding \(b,c\) as well gives the Schur-complement identity \(G_S=G_a|_{V\setminus S}-G_a|_{V\setminus S,U}(G_a|_{U,U})^{-1}G_a|_{U,V\setminus S}\). Summing its diagonal, using \(H\mathbf1=0\), and accounting for the two eliminated diagonal terms yields the exact two-by-two formula
\[
J_{m,n}(S)=\operatorname{tr}H+NH_{aa}-\operatorname{tr}(M^{-1}Z),
\]
where \(M_{uv}=H_{uv}-H_{ua}-H_{av}+H_{aa}\), and
\[
Z_{uv}=(H^2)_{uv}-(H^2)_{ua}-(H^2)_{av}+(H^2)_{aa}+N(H_{aa}-H_{au})(H_{aa}-H_{av}),\qquad u,v\in U.
\]
Here \(M\) is positive definite because distinct grounded vertices give a positive definite Green principal submatrix. The shared constant is
\[
\operatorname{tr}H+NH_{aa}=\frac{2(m^2n^2+m^2n-m^2+mn^2-mn-n^2)}{mn(m+n)}.
\]

Coordinate permutations reduce all triples to exactly six possibilities when \(3\le m<n\): a matching \(D=\{(0,0),(1,1),(2,2)\}\); two-first-row \(B_m=\{(0,0),(0,1),(1,2)\}\); its transposed type \(B_n=\{(0,0),(1,0),(2,1)\}\); a corner \(C=\{(0,0),(0,1),(1,0)\}\); all-first-row \(T_m=\{(0,0),(0,1),(0,2)\}\); and all-second-coordinate \(T_n=\{(0,0),(1,0),(2,0)\}\). This list is exhaustive because each of the two coordinate-equality partitions of three labels is either all distinct, one repeated pair, or all equal, and distinct vertices cannot repeat the same pair in both coordinates.

Substitution into the explicit two-by-two formula gives rational differences \(J_X-J_D=P_X/Q_X\). The denominators \(Q_X\), respectively in the order \(B_m,B_n,C,T_m,T_n\), are
\[
\begin{aligned}
&3m(m+n)(n+1)(mn+m+n)(3mn+3m+4n),\\
&3n(m+1)(m+n)(mn+m+n)(3mn+4m+3n),\\
&3mn(m+n)(mn+m+n)(3mn+4m+4n+4),\\
&3m(m+n)(n+1)(mn+m+n),\\
&3n(m+1)(m+n)(mn+m+n).
\end{aligned}
\]
These are strictly positive for the stated dimensions. The five numerator polynomials, upon the simultaneous substitution \(m=3+x\), \(n=4+x+y\), with \(x,y\ge0\), contain, respectively, \(30,26,30,18,15\) nonzero monomials, **all with strictly positive integer coefficients**; their total degrees are \(7,7,7,5,5\). This is an exact finite polynomial certificate (constructed and rechecked without floating-point arithmetic by the accompanying `verify.py`, directly from the displayed projector formula). Consequently \(J_D<J_X\) for all five other configurations whenever \(3\le m<n\).

For \(m=2<n\), only \(B_m,C,T_m\) remain feasible, and the exact comparisons simplify to
\[
J_C-J_{B_m}=\frac{2(5n^4+15n^3+30n^2+39n+18)}{n(n+1)(n+2)(5n+3)(5n+6)}>0,
\]
\[
J_{T_m}-J_{B_m}=\frac{2(5n^3+10n^2+2n-6)}{3(n+1)(n+2)(5n+3)}>0.
\]
These strict inequalities hold for all integers \(n\ge3\). Finally, permutation counting gives the stated multiplicities of optimizers. Substitution in the two-by-two formula gives both optimal-value rational functions, completing the proof.

## Verification
Run `python verify.py` using `requirements.txt`. The standalone checker recomputes the spectral projectors and six orbit costs symbolically; exactly compares the five differences, certifies positivity of every coefficient after the dimension substitutions, confirms the two-row strict inequalities, and cross-checks 37 representative rational costs against directly inverted grounded Laplacians. It also tests the exceptional four-vertex case. The supplied `verification_output.txt` is a recorded run; the proof rests on the exact algebra and finite symbolic coefficient certificates, not on numerical extrapolation.

## Relationship to prior work
Fitch and Leonard (first arXiv version 7 July 2014; 2016 journal publication) derive joint centrality for arbitrary noise-free leader sets, and give explicit location theorems for cycles and paths; their inspected article does not supply the rectangular rook-graph three-leader classification. Patterson, Yi and Zhang (arXiv 2017) derive resistance-based leader-selection methods and special network examples, but their inspected analysis does not establish this product-graph optimizer. These general identity and optimization frameworks are not claimed as new. The present contribution is the complete three-leader structural classification for strictly unequal factor sizes, including exact minimum values, optimizer counts, and a strict two-row boundary. The equal-factor strongly regular case is excluded because it is covered by an earlier general three-leader theorem.

## Limitations
The proof applies only to unweighted **strictly rectangular** rook graphs with \(m<n\) and exactly three noise-free leaders. It does not establish robustness under heterogeneous conductances, different noise covariances, or four or more leaders. An overlooked specialized or unindexed equivalent theorem remains an originality risk. The polynomial certificates are exact and reproducible but rely on the displayed symbolic identities; a separate independent mathematical audit has not been performed.

## References
- K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, first posted 2014-07-07, arXiv:1407.1569; IEEE Transactions on Control of Network Systems 3 (2016), 366–378, DOI:10.1109/TCNS.2015.2481138. Author manuscript: https://naomi.princeton.edu/wp-content/uploads/sites/744/2021/03/FitLeoTCNS2016.pdf
- S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, first posted 2017-08-23, arXiv:1708.06873, https://arxiv.org/pdf/1708.06873.
- J. Ducey, J. Gerhard and N. Watson, *The Smith and Critical Groups of the Square Rook’s Graph and its Complement*, The Electronic Journal of Combinatorics 23 (2016), P4.9, DOI:10.37236/5442 (background rook-graph algebra, not a leader-placement theorem).
