# A sharp representation-mode transition in Hilbert snowflakes of diameter-three Kneser graphs

## Finding
For every integer \(k\ge8\), let \(G_k=KG(3k-2,k)\): its vertices are the \(k\)-subsets of a \((3k-2)\)-element set, with edges joining disjoint subsets and unit-edge shortest-path distance \(d\). Put
\[
N_k=\binom{3k-2}{k},\quad B_k=\binom{2k-4}{k-2},\quad r_k=k-5+\frac1{k-1}.
\]
There is exactly one positive real \(p_k\) satisfying
\[
\boxed{B_k\{r_k(3^{p_k}-2^{p_k})-(2^{p_k}-1)\}=2^{p_k}.}
\]
The supremal negative-type exponent of \((V(G_k),d)\) is **exactly** \(p_k\). Equivalently \(d^{p/2}\) is real-Hilbert-isometric if and only if \(0<p\le p_k\). The least affine embedding dimension is \(N_k-1\) at every \(0<p<p_k\), and drops exactly to
\[
\boxed{N_k-1-\left(\binom{3k-2}{2}-(3k-2)\right)}
\]
at \(p=p_k\). The sole critical nullspace is the second nontrivial Johnson-scheme representation, not the first or any odd-indexed representation. Moreover
\[
\boxed{p_k\sim\frac1{B_k\,[r_k\log(3/2)-\log2]}\sim\frac1{kB_k\log(3/2)}}\qquad(k\to\infty).
\]
The lower limit \(k=8\) is **sharp for this controlling-representation law**. On \(G_7=KG(19,7)\), at exponent \(p=1/100\), the second-representation powered-distance eigenvalue is negative while the third-representation eigenvalue is positive. Thus the second representation cannot control the first loss of negative type at \(k=7\). No value of the critical exponent for \(k=7\) is claimed here.

## Assumptions and scope
A metric has \(p\)-negative type when \(\sum_{x,y}c_xc_y d(x,y)^p\le0\) for every real zero-sum vector \(c\). Strictness means inequality for every nonzero such vector. Hilbert-isometric snowflakes use the norm distance \(d^{p/2}\), with no bound on ambient dimension. All asymptotics run through positive integer \(k\). The graph is unweighted, simple and finite. Its vertex count is \(N_k\). The result does not concern general Kneser parameters or arbitrary bilipschitz distortions.

## Proof
First, for \(k\ge3\) and \(n=3k-2\), two distinct \(k\)-sets are at graph distance \(1\) if disjoint, at distance \(3\) if their intersection has size \(1\), and at distance \(2\) otherwise. A distance-two path exists precisely when the union fits outside another \(k\)-set, equivalently intersection size at least \(2\). When intersection is one, a distance-three path is obtained by choosing a neighbor containing the \(k-1\) points of the second set outside their intersection and one point outside their union, then finding a common neighbor with that second set. This gives diameter three.

Let \(A_k\) denote adjacency on disjoint \(k\)-sets, \(A_{k-1}\) adjacency on sets meeting in one point, and \(A_1\) adjacency on sets differing in one point in the Johnson scheme. For \(t=2^p\), \(u=3^p\), the powered-distance matrix is
\[
D_p=t(J-I)-(t-1)A_k+(u-t)A_{k-1}.
\]
The Johnson scheme decomposes the orthogonal complement of constants into invariant subspaces \(E_j\), \(1\le j\le k\), of dimensions \(\binom{n}{j}-\binom{n}{j-1}\). Their established eigenvalues for \(A_k\) and \(A_1\) are respectively
\[
b_j=(-1)^j\binom{2k-2-j}{k-j},\qquad
\theta_j=(k-j)(2k-2-j)-j.
\]
These standard formulas can be reconstructed from nested inclusion-vector spaces for \(j\)-subsets by inclusion-exclusion; the independent binomial inclusion-sum identities are also checked in the accompanying exact script. A direct common-neighbor count supplies the further identity
\[
A_kA_1=k(k-2)A_k+(k-1)A_{k-1}.
\]
Indeed a disjoint pair contributes \(k(k-2)\) single swaps, whereas a one-point-intersection pair contributes \(k-1\), and all other intersection classes contribute zero. Thus the \(A_{k-1}\)-eigenvalue on \(E_j\) is \(b_jr_j\), where
\[
r_j=\frac{\theta_j-k(k-2)}{k-1}
=\frac{k^2-3kj+j(j+1)}{k-1}.
\]
The exact \(D_p\)-eigenvalue on \(E_j\) is therefore
\[
\Lambda_j(p)=-t+b_j\{r_j(u-t)-(t-1)\}.
\]

For \(j=2\), \(b_2=B_k>0\) and \(r_2=r_k\). The function
\[
\frac{\Lambda_2(p)}{2^p}=-1+B_k\left\{r_k((3/2)^p-1)-(1-2^{-p})\right\}
\]
starts at \(-1\) and increases strictly for every \(p\ge0\), since \(r_k\ge22/7>\log2/\log(3/2)\). It tends to infinity, so its unique positive zero is the stated \(p_k\).

We show that **every other** \(\Lambda_j(p_k)\) is strictly negative, uniformly in \(k\ge8\). Put \(h=u-t>0\), \(x=(t-1)/h\), and \(c=\log2/\log(3/2)<7/4\). The elementary bounds \(1-e^{-a}\le a\) and \(e^b-1\ge b\) give \(0<x\le c\). The sequence \(r_j\) is strictly decreasing in \(j\), with \(r_1=k-2\), \(r_3\ge4/7\), and \(r_k=-k\). Write \(B_j=|b_j|\). It decreases with \(j\), and \(B_3/B_2=1/2\), \(B_j/B_2<1/8\) for \(j\ge5\). At the critical point \(t=B_2h(r_2-x)\). For any even \(j>2\), if \(r_j-x\le0\) then \(\Lambda_j<0\); otherwise \(B_j(r_j-x)<B_2(r_2-x)\) implies the same conclusion. For odd \(j\),
\[
\Lambda_j=-t+B_jh(x-r_j).
\]
For \(j=1\) this is negative since \(r_1>c\). For \(j=3\), \((B_3/B_2)(x-r_3)\le c/2<r_2-c\). For all odd \(j\ge5\),
\[
\frac{B_j}{B_2}(x-r_j)<\frac{k+7/4}{8}
< k-5+\frac1{k-1}-\frac74\le r_2-x,
\]
where the middle inequality holds for every \(k\ge8\) (already strict at \(8\), and the gap increases). Therefore all odd eigenvalues are strictly negative. The sole zero eigenvalue at the critical exponent lies on \(E_2\), of multiplicity \(\binom n2-n\).

By Schoenberg's finite-metric theorem, conditional negativity of \(D_p\) is equivalent to an isometric Hilbert embedding of \(d^{p/2}\), and the minimal affine embedding dimension is the rank of the centered Gram matrix \(-\tfrac12P D_pP\). The strict spectrum just proved gives the stated ranks. Every smaller positive exponent is also of negative type by the standard closure of conditionally negative powers under \(0<q\le p\); every larger exponent fails, since \(\Lambda_2(p)/2^p\) stays positive.

The uniqueness equation and Taylor expansion at zero yield \(p_k\sim [B_k(r_k\log(3/2)-\log2)]^{-1}\): \(B_k r_k\to\infty\), the unique root tends to zero, and the quadratic Taylor remainder at that root is lower order. Since \(r_k\sim k\), the second equivalence follows.

Finally, for \(k=7\), \(b_2=252\), \(r_2=13/6\), \(b_3=-126\), and \(r_3=-1/3\). At \(p=1/100\), exact rational bounds established by raising to the \(100\)th power are
\[
\frac{1006955}{10^6}<2^{1/100}<\frac{1006956}{10^6},\qquad
\frac{1011046}{10^6}<3^{1/100}<\frac{1011047}{10^6}.
\]
Substituting these bounds in the two explicit eigenvalues proves \(\Lambda_2(1/100)<-0.525\) and \(\Lambda_3(1/100)>0.041\). Therefore the second mode cannot control \(k=7\); the claimed cutoff is sharp.

## Verification
Run `python3 check_kneser.py` (Python standard library only). This standalone program independently computes the Johnson intersection-one eigenvalues by an inclusion-binomial formula, checks the adjacency-product eigenvalue identity for all indices in orders \(3\) through \(30\), and verifies the two rational-power enclosures and strict \(k=7\) eigenvalue signs by exact integer arithmetic. Its observed result was `KNESER_NEGATIVE_TYPE_CHECK_OK association_eigenvalues= 462 boundary_j2_upper= -0.525383 boundary_j3_lower= 0.041197`. Its finitely many checks are not the infinite proof: that is the comparison of all representation modes for every \(k\ge8\) above.

## Relationship to prior work
Robertson (2020) and Sánchez (2011) give general negative-type criteria for finite metrics, but not the sharp Kneser distance-three representation cutoff stated here. The Johnson-scheme and Kneser adjacency spectra are classical and expressly used as prior facts. The nearest studied geometry in Cioabă, Gupta, Ihringer and Kurihara (2021) concerns **bilipschitz Euclidean distortion of distance-regular graphs**, and does not imply the computed negative-type exponent for the present diameter-three Kneser sequence. The natural diameter-two Kneser threshold follows directly from the most negative adjacency eigenvalue and is not claimed here. The novelty claim is restricted to the \(k\ge8\) mode-comparison theorem, its sharp \(k=7\) exclusion, endpoint rank, and exponential asymptotic.

## Limitations
Only the first diameter-three Kneser family \(KG(3k-2,k)\) for \(k\ge8\) is classified. The \(k=7\) calculation is a boundary obstruction, not a full exponent computation. The argument assumes the standard Johnson adjacency spectra, for which an independent finite binomial check is supplied; no independent mathematical audit or priority certification has been conducted. An earlier equivalent calculation within association-scheme literature remains a residual historical-priority risk.

## References
- Gavin Robertson, *The Maximal Generalised Roundness of Finite Metric Spaces*, arXiv:2004.10923, first publicly posted 2020-04-23; https://arxiv.org/abs/2004.10923 .
- Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451, first publicly posted 2011-08-02; https://arxiv.org/abs/1108.0451 .
- Sebastian M. Cioabă, Himanshu Gupta, Ferdinand Ihringer, and Hirotake Kurihara, *The least Euclidean distortion constant of a distance-regular graph*, arXiv:2109.09708, first publicly posted 2021-09-20; https://arxiv.org/abs/2109.09708 .
- Andries E. Brouwer, Sebastian M. Cioabă, Ferdinand Ihringer and Matt McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, J. Combin. Theory Ser. B 133 (2018), 88–121 (background association-scheme eigenvalues).
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. 44 (1938), 522–536 (negative-type embedding criterion).
