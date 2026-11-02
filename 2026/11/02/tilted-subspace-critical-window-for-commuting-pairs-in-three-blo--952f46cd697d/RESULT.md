# Tilted-subspace critical window for commuting pairs in three-block unipotent radicals

## Finding
For every prime power \(q\) and positive integers \(a,b,c\), let \(G_{a,b,c}(q)\) consist of block-unipotent matrices
\[
g(X,Y,Z)=\begin{pmatrix}I_a&X&Z\\0&I_b&Y\\0&0&I_c\end{pmatrix},
\quad X\in M_{a\times b}(\mathbb F_q),\quad Y\in M_{b\times c}(\mathbb F_q),\quad Z\in M_{a\times c}(\mathbb F_q).
\]
Choose independent uniform \(g=g(X,Y,Z)\) and \(h=g(X',Y',Z')\). Put \(m=2b\) and \(W=\operatorname{rowspan}[X,-X']\le\mathbb F_q^m\). Conditional on \(gh=hg\), each individual subspace \(S\le\mathbb F_q^m\) of dimension \(r\) has probability
\[
\Pr(W=S\mid gh=hg)=\frac{q^{(a-c)r}\prod_{i=0}^{r-1}(1-q^{i-a})}{\displaystyle\sum_{T\le\mathbb F_q^m}q^{(a-c)\dim T}\prod_{i=0}^{\dim T-1}(1-q^{i-a})}.
\tag{1}
\]
Empty products equal \(1\); any factor with \(i=a\) makes the product zero. Therefore this formula is valid even for \(a<m\).

Fix \(q\) and \(b\), and let \(a,c\to\infty\). If \(a-c=\delta\) eventually for an integer \(\delta\), the conditional law of \(W\) converges in total variation at rate \(O_{q,b,\delta}(q^{-a})\) to the tilted counting measure
\[
\boxed{\quad\mu_\delta(S)=\frac{q^{\delta\dim S}}{C_{m,q}(\delta)},\qquad C_{m,q}(\delta)=\sum_{r=0}^m{m\brack r}_q q^{\delta r}.\quad}
\tag{2}
\]
In the **balanced window** \(a=c\to\infty\), the limiting law is exactly uniform over the *entire subspace lattice*, not uniform over dimensions. In particular, when \(b=1\) and \(q=2\), the limiting rank probabilities for dimensions \(0,1,2\) are \(1/5,3/5,1/5\). If instead \(a-c\to+\infty\) with both outer dimensions tending to infinity, the conditional rowspace equals all of \(\mathbb F_q^m\) with probability tending to \(1\). If \(a-c\to-\infty\), it equals the zero subspace with probability tending to \(1\). Thus a fixed-width critical window separates two extreme concentration regimes.

The exact (unconditional) commuting probability, supplied as a derivation tool rather than claimed as a new class-number enumeration, is
\[
\Pr(gh=hg)=q^{-am}\sum_{r=0}^{\min(a,m)}{m\brack r}_q q^{(a-c)r}\prod_{i=0}^{r-1}(1-q^{i-a}).
\tag{3}
\]
Here \({m\brack r}_q\) denotes the Gaussian binomial coefficient, the number of dimension-\(r\) subspaces of \(\mathbb F_q^m\).

## Assumptions and scope
The matrices are over an arbitrary finite field \(\mathbb F_q\) of prime-power cardinality \(q\), in any characteristic. The block sizes \(a,b,c\) are positive integers. Equations (1) and (3) are finite exact identities for all such parameters. For (2) and the extreme limits, \(q\) and \(b\) are fixed while both \(a\) and \(c\) diverge. The balanced assertion concerns *commuting pairs* conditional on a group-theoretic event; it does not assert that the unconditional rowspace is uniformly distributed.

## Proof
Matrix multiplication gives
\[
g(X,Y,Z)g(X',Y',Z')=g(X+X',Y+Y',Z+Z'+XY'),
\]
so \(gh=hg\) if and only if \(XY'=X'Y\). Writing
\[
A=[X,-X']\in M_{a\times m}(\mathbb F_q),\qquad B=\begin{bmatrix}Y'\\Y\end{bmatrix}\in M_{m\times c}(\mathbb F_q),
\]
the commutation equation becomes \(AB=0\). The map from the four off-central blocks to the pair \((A,B)\) is bijective, and under uniform sampling these are independent uniform matrices. The central blocks \(Z,Z'\) cancel completely and need no further normalization.

Fix any subspace \(S\le\mathbb F_q^m\) of dimension \(r\). The number of matrices \(A\in M_{a\times m}(\mathbb F_q)\) with rowspace exactly \(S\) is the number of surjective maps \(\mathbb F_q^a\to S\), namely
\[
\prod_{i=0}^{r-1}(q^a-q^i).
\]
For each such \(A\), the equation \(AB=0\) allows exactly \(q^{(m-r)c}\) matrices \(B\), because each column lies in the \((m-r)\)-dimensional kernel of \(A\). Consequently the number of commuting pairs of off-central blocks with \(W=S\) is
\[
q^{mc}\,q^{(a-c)r}\prod_{i=0}^{r-1}(1-q^{i-a}).
\]
The factor \(q^{mc}\) is independent of \(S\); dividing by the sum over all subspaces proves (1). Summing over dimensions, with \({m\brack r}_q\) choices of \(S\) for each \(r\), and dividing by the full count \(q^{am+mc}\) of pairs \((A,B)\), gives (3).

For the limiting law, write \(\alpha_a(r)=\prod_{i=0}^{r-1}(1-q^{i-a})\). For \(a\ge m\) and \(0\le r\le m\),
\[
0\le 1-\alpha_a(r)\le\sum_{i=0}^{m-1}q^{i-a}=\frac{q^m-1}{q-1}q^{-a}.
\tag{4}
\]
If \(a-c=\delta\) is fixed, replacing every \(\alpha_a(r)\) by \(1\) in (1) therefore produces the measure (2), with total variation error \(O_{q,b,\delta}(q^{-a})\) because the state space is finite and its limiting normalizer is positive. When \(\delta=0\), all individual subspaces have the same limiting weight.

If \(a-c\to+\infty\), divide the weights in (1) by the weight of the unique full subspace \(\mathbb F_q^m\): its \(\alpha_a(m)\to1\), while every proper subspace has the additional factor \(q^{-(a-c)(m-r)}\to0\). If \(a-c\to-\infty\), the unique zero subspace has weight \(1\), and every positive-dimensional subspace has a factor \(q^{(a-c)r}\to0\). This proves the two off-critical concentration assertions. No limiting interchange in \(q\) or \(b\) is invoked.

## Verification
The accompanying standalone `verify.py` independently enumerates all four noncentral block matrices and checks the group commutation equation over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), including a case with a two-dimensional middle block. For nine parameter configurations it confirms the exact commuting-pair count, every rank-stratum count, and the *individual rowspace* weight, not merely the total count. Six supplementary numerical comparisons check the balanced normalization against the entire subspace-lattice count at outer dimensions \(6\) and \(10\). Run `python3 verify.py`; its final line must be `VERIFY_OK 9 exhaustive cases plus 6 diagonal-limit checks`.

The finite checks are corroborative: the unrestricted statements follow from the counting proof and estimate (4).

## Relationship to prior work
Garge–Sharma–Singh, arXiv:2105.12930v1 (first public May 27, 2021; primary subject classification 20G15), studies asymptotic commuting probabilities in algebraic and finite reductive groups as the **number of commuting tuple entries** grows. The present question instead fixes the tuple length at two, varies outer block dimensions of a nilpotent unipotent radical, and conditions on the actual cross-block rowspace. Neither its reductive-group asymptotic nor its tuple-length parameter yields the present fixed-middle-width subspace-valued law. The literature on commuting probabilities in triangular and unitriangular groups includes Kaur–Sharma–Singh, arXiv:2006.01493v1 (first public June 2, 2020), whose computations cover ordinary unitriangular groups of small sizes and higher commuting tuples. Goodwin–Röhrle, arXiv:0901.0667, proved polynomiality of class numbers for all unipotent radicals associated with flags of length at most five, hence includes the present three-block groups. Those class-number results and elementary finite-matrix rank counts are prior work, not the asserted new contribution.

The distinction is **conditioning on commutativity and retaining the actual rowspace of a two-copy cross-block matrix**, followed by the fixed-middle-width, large-outer-block critical window. Aggregate conjugacy counts or class-size spectra do not by themselves determine this rowspace-valued conditional law. Earlier analyses of three-block groups with simultaneously growing middle and outer dimensions yield a different large-rank scaling regime; a theta-type rank limit in that regime does not imply the finite subspace-lattice transition with fixed \(b\). The closest detailed sources were compared on the observable, the varying parameters and the logical implications, rather than by terminology alone.

## Limitations
The measure is conditional on a potentially rare commuting event; no claim is made about random noncommuting pairs. The total-variation rate is uniform only with fixed \(q,b,\delta\). The theorem does not classify conjugacy classes, all commuting \(k\)-tuples, or representations of the group. An earlier general zero-product random-matrix theorem could provide an alternative derivation of the conditional law; no global publication-priority certification or independent mathematical audit is claimed.

## References
1. S. M. Garge, U. B. Sharma and A. Singh, *Asymptotics of Commuting Probabilities in Reductive Algebraic Groups*, arXiv:2105.12930v1 (May 27, 2021), especially Introduction and Theorems 4.1 and 5.4.
2. D. Kaur, U. B. Sharma and A. Singh, *Branching Rules and Commuting Probabilities for Triangular and Unitriangular Matrices*, arXiv:2006.01493v1 (June 2, 2020), especially Introduction and Section 8.
3. S. M. Goodwin and G. Röhrle, *Counting Conjugacy Classes in the Unipotent Radical of Parabolic Subgroups of GL_n(q)*, arXiv:0901.0667 (first submitted January 2009), especially Theorem 1.2 and Section 3.
4. S. Eberhard, *Commuting probabilities of finite groups*, Bull. London Math. Soc. 47 (2015), 796–808, doi:10.1112/blms/bdv050 (background on the group invariant).
