# Complete alternating-rank spectra and graphical-group character degrees for complete tripartite graphs

## Finding

Let \(q\) be any prime power, let \(a,b,c\ge2\) be integers, and put \(n=a+b+c\) and \(m=ab+ac+bc\). Let \(N_q(a,b,c;t)\) be the number of alternating matrices over \(\mathbb F_q\), of order \(n\), having rank \(2t\), whose only potentially nonzero entries are the cross-part entries of the complete tripartite graph \(K_{a,b,c}\). Each cross-part entry is an independent field element; entries inside a part and on the diagonal vanish.

For \(0\le k\le\min(u,v)\), define
\[
R_q(u,v,k)=\prod_{i=0}^{k-1}\frac{(q^u-q^i)(q^v-q^i)}{q^k-q^i},
\]
with \(R_q(u,v,k)=0\) outside that range. For \(0\le h\le r\), let
\[
I_q(r,h)=\prod_{i=0}^{h-1}\frac{q^{2(r-i)}-1}{q^{h-i}-1},
\]
with \(I_q(r,h)=0\) otherwise. Write \({u\brack v}_{Q}\) for the Gaussian binomial coefficient, taken as zero unless \(0\le v\le u\). Define the *symplectic pullback rank enumerator*
\[
H_q(r,d,j)=\sum_{k=0}^{\min(2r,d)}\!\mathbf1_{\substack{h=k-2j\ge0\\h\le r-j}}\,
I_q(r,h)\,q^{2j(r-h-j)}{r-h\brack j}_{q^2}
\prod_{i=0}^{k-1}(q^d-q^i).
\]
In particular, \(H_q(0,d,0)=1\), and all products over empty index ranges equal one.

**Exact rank distribution.** For every integer \(t\ge0\),
\[
\boxed{
N_q(a,b,c;t)=
\sum_{r=0}^{\min(a,b)}\ \sum_{s=0}^{\min(a+b-2r,c)}
R_q(a,b,r)R_q(a+b-2r,c,s)q^{2rs}
H_q(r,c-s,t-r-s).}
\]
The convention is \(H_q(r,d,j)=0\) when \(j<0\). The distribution is exact, satisfies \(\sum_tN_q(a,b,c;t)=q^m\), and is valid also in characteristic two.

**Character-degree consequence.** For odd \(q\), let \(G_{a,b,c}(\mathbb F_q)\) denote the standard class-two graphical group associated with \(K_{a,b,c}\): it has generators corresponding to vertices and independent central edge directions, and its commutator bilinear form is the above edge-supported alternating matrix. Then for every \(t\ge0\),
\[
\boxed{\#\{\chi\in\operatorname{Irr}(G_{a,b,c}(\mathbb F_q)):\chi(1)=q^t\}
=q^{n-2t}N_q(a,b,c;t).}
\]
These are all its ordinary irreducible characters. Both displayed formulas constitute one exact finite-field counting theorem.

For example, \(K_{2,2,2}\) has, over \(\mathbb F_3\), rank multiplicities \(N_3(2,2,2;t)=(1,1376,198288,331776)\) for ranks \(0,2,4,6\), respectively. Consequently its graphical group has \((729,111456,1784592,331776)\) irreducible characters of respective degrees \((1,3,9,27)\). The weighted degree-square sum is \(3^{18}\), the group order.

## Assumptions and scope

An alternating form means a bilinear form \(\beta\) with \(\beta(v,v)=0\), irrespective of field characteristic; an alternating matrix is skew-symmetric with zero diagonal (symmetric with zero diagonal in characteristic two). The matrix space has exactly \(m=ab+ac+bc\) free coordinates. We count labeled matrices, not congruence classes. An integer parameter outside a sum's stated range has zero contribution. The character application uses odd \(q\); the matrix theorem itself has no such restriction. The hypotheses \(a,b,c\ge2\) exclude cone graphs \(K_{1,a,b}\) already covered by the known coning recurrence.

The finite-field graphical group is the usual class-two, exponent-\(p\) group constructed from the alternating edge-commutator map on the \(n\)-dimensional vertex space with center an \(m\)-dimensional edge space; for odd characteristic this may be realized on the vector space \(V\oplus Z\) by \((v,z)(v',z')=(v+v',z+z'+\tfrac12[v,v'])\). Its order is \(q^{n+m}\).

## Proof

**Lemma 1 (image-radical census).** Let \(J\) be any fixed nondegenerate alternating form on \(\mathbb F_q^{2r}\). For every \(d\ge0\), the number of linear maps \(T:\mathbb F_q^d\to\mathbb F_q^{2r}\) with \(\operatorname{rank}(T^{\mathsf T}JT)=2j\) equals \(H_q(r,d,j)\).

*Proof.* Stratify \(T\) by its image dimension \(k\). Every map onto a fixed \(k\)-dimensional subspace has \(\prod_{i=0}^{k-1}(q^d-q^i)\) choices. Write \(W=\operatorname{im}T\) and \(R=W\cap W^\perp\). If the restricted alternating form has rank \(2j\), then \(h=\dim R=k-2j\). The radical \(R\) must be a totally isotropic \(h\)-plane. Counting ordered isotropic flags successively, or dividing by the number of bases of an \(h\)-plane, gives precisely \(I_q(r,h)\) possibilities. For a fixed \(R\), the image \(W/R\) is a nondegenerate \(2j\)-plane in the \(2(r-h)\)-dimensional symplectic quotient \(R^\perp/R\). Its number is
\[
\frac{|\operatorname{Sp}_{2(r-h)}(q)|}{|\operatorname{Sp}_{2j}(q)|\,|\operatorname{Sp}_{2(r-h-j)}(q)|}
=q^{2j(r-h-j)}{r-h\brack j}_{q^2}.
\]
Conversely, each such \(R\) and nondegenerate quotient plane has exactly one preimage \(W\) containing \(R\); its radical is \(R\). Thus multiplication by the surjection count and summing \(k\) gives \(H_q(r,d,j)\). This uses only symplectic linear algebra, valid for all characteristics. \(\square\)

**Lemma 2 (two-step alternating elimination).** Suppose a block of the form
\[
B=\begin{pmatrix}0_a&X&Y\\-X^{\mathsf T}&0_b&Z\\-Y^{\mathsf T}&-Z^{\mathsf T}&0_c\end{pmatrix}
\]
has \(X\in M_{a\times b}(\mathbb F_q)\) of rank \(r\), with \(Y,Z\) arbitrary. Put \(d=a+b-2r\). Conditioned on this fixed \(X\), the number of \((Y,Z)\) for which \(\operatorname{rank}B=2r+2s+2j\) is
\[
R_q(d,c,s)\,q^{2rs}\,H_q(r,c-s,j),
\]
summed over the possible values of \(s\) and \(j\) giving the chosen overall rank.

*Proof.* Invertible changes of bases in the first two parts bring \(X\) to a rectangular identity of rank \(r\), without changing the uniform count of \((Y,Z)\). The first \(2r\) coordinates become a nondegenerate hyperbolic block \(J\); the remaining \(d\) coordinates in those parts span a null subspace. The cross-coordinates with the third part therefore split bijectively into arbitrary matrices \(T\in M_{2r\times c}\) and \(U\in M_{d\times c}\). Schur-complement congruence on \(J\) reduces the rank to
\[
2r+\operatorname{rank}\begin{pmatrix}0_d&U\\-U^{\mathsf T}&C\end{pmatrix},\qquad C=T^{\mathsf T}J^{-1}T
\]
(up to an irrelevant sign). If \(\operatorname{rank}U=s\), independent basis changes reduce \(U\) to an identity block of size \(s\); eliminating its paired hyperbolic \(2s\)-space leaves exactly the restriction \(C|_{\ker U}\). Thus
\[
\operatorname{rank}B=2r+2s+\operatorname{rank}(T_0^{\mathsf T}J^{-1}T_0),
\]
where \(T_0\) is the restriction of \(T\) to the \((c-s)\)-dimensional subspace \(\ker U\). There are \(R_q(d,c,s)\) possible \(U\). For each one, the values of \(T\) on a complementary \(s\)-space are freely chosen in \(q^{2rs}\) ways, and Lemma 1 counts its restriction \(T_0\) with pullback rank \(2j\) as \(H_q(r,c-s,j)\). \(\square\)

**Completion of the rank formula.** The upper-right \(a\times b\) block \(X\) has rank \(r\) in exactly \(R_q(a,b,r)\) ways. Applying Lemma 2 for every \(r\), then summing over \(s\) with \(j=t-r-s\), gives the boxed formula. Every edge specialization has appeared exactly once, proving also the total \(q^m\) count. Since both reductions were congruences and Lemma 1 holds over all finite fields, there is no characteristic restriction. \(\square\)

**Character consequence.** For odd \(q\), fix a linear character of the central edge space, equivalently a label \(y\in\mathbb F_q^m\) after choosing a nontrivial additive character. Its commutator pairing on the vertex quotient is the alternating form \(B(y)\). If this has rank \(2t\), its radical has dimension \(n-2t\). The irreducibles lying above the chosen central character are parametrized by the \(q^{n-2t}\) characters of the radical, each of degree \(q^t\), by the elementary finite Heisenberg/Stone–von Neumann representation decomposition. This also follows from the graphical-group character-rank theorem in the references. Summing over labels of rank \(2t\) proves the second box. The degree-square check is
\[\sum_t q^{n-2t}N_q(a,b,c;t)(q^t)^2=q^{n+m}=|G|.\]
\(\square\)

## Verification

The standalone `artifacts/verify.py` requires only Python 3 standard-library modules. Running `python3 artifacts/verify.py` from a directory containing this document and the script exhaustively constructs every alternating matrix for twelve parameter combinations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\). It compares the directly enumerated rank histogram with the closed formula. The three-part cases include \(K_{2,2,2}\) for both \(q=2\) and \(q=3\), and \(K_{2,2,3}\) for \(q=2\). A second suite directly enumerates eight symplectic-pullback rank histograms and verifies 125 pullback count normalizations. The script returns `EXHAUSTIVE_CASES 12 DIRECT_PULLBACK_CASES 8 PULLBACK_CHECKS 125 VERIFY_OK`. These are finite cross-checks, not a substitute for the all-parameter proof.

For the displayed \(K_{2,2,2}\) example at \(q=3\), the rank counts sum to \(3^{12}=531441\). The character-degree weighted square sum is \(3^{18}\), as required for a group of order \(3^{6+12}\).

## Relationship to prior work

Rossmann (2022) explicitly poses the degree-multiplicity question for graphical groups (Question 1.10) and identifies edge-supported alternating ranks as the key invariant. Rossmann and Voll (2025), Theorem A, prove a join formula for ask zeta functions that encode *averages of kernel sizes over finite quotient rings*. This is broader in graph operations but does not give a distribution resolved by each individual alternating rank in the stated results. The preprint was first public on 2025-05-15.

A separate coning-recurrence result determines the complete rank distribution under addition of a *single universal vertex* and gives explicit formulas for \(K_{1,a,b}\) and its iterated cones; this prior theorem was inspected in full. Every vertex of \(K_{a,b,c}\), with \(a,b,c\ge2\), has at least one non-neighbor, so these graphs are not obtainable from a smaller graph by coning. The current result instead uses the rank of an arbitrary rectangular first cross-block and a symplectic pullback census. Known tree and cycle rank enumerators have different graph domains. The explicit character-degree consequence uses the already known character-rank conversion, not a new representation-theoretic equivalence.

## Limitations

The complete formula is a finite nested sum and is not asserted to be a minimal expression or coefficientwise polynomial in \(q\); although each count is integer-valued, polynomiality of each coefficient is not separately proved here. No assertion is made about arbitrary graph joins or about character theory in even characteristic. Complete multipartite examples with singleton parts are intentionally excluded because a coning formula already covers those.

The full implications of older general ask-zeta results for rank-specific questions may admit alternate approaches; the literature search does not establish universal priority. Exhaustive computations cover only the finite cases listed.

## References

1. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” *Bulletin of the London Mathematical Society* **54** (2022), DOI 10.1112/blms.12665, Section 1.6, Question 1.10. https://doi.org/10.1112/blms.12665
2. T. Rossmann and C. Voll, “Ask zeta functions of joins of graphs,” arXiv:2505.10263 (first public 15 May 2025), Theorem A and Sections 1 and 11. https://arxiv.org/abs/2505.10263
3. “Coning recurrence for character degrees of graphical groups,” public mathematical note (2026), available at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-coning-recurrence-for-character-degrees-of-graphical-groups--732adc755a75
4. T. Rossmann, “Ask zeta functions associated with small graphs,” computed tables of average-kernel zeta functions, https://torossmann.github.io/cico/
