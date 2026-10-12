# Joint rank and common-kernel distribution of mutually annihilating square-zero matrix pairs

## Finding
For every prime power \(q\), integer \(n\ge1\), and integers \(0\le r,s,k\le n\), let \(C_{n,q}(r,s,k)\) count ordered pairs \((X,Y)\) of \(n\times n\) matrices over \(\mathbb F_q\) for which
\[
X^2=Y^2=XY=YX=0,\quad \operatorname{rank}X=r,\quad \operatorname{rank}Y=s,\quad \dim(\ker X\cap\ker Y)=k.
\]
Define the rank-map count
\[
R_q(a,b,t)={a\brack t}_q{b\brack t}_q\prod_{i=0}^{t-1}(q^t-q^i),
\]
where \({u\brack v}_q\) counts \(v\)-subspaces of \(\mathbb F_q^u\), and is zero when \(v<0\) or \(v>u\). Empty products equal \(1\). Then the complete joint spectrum is
\[
\boxed{C_{n,q}(r,s,k)={n\brack k}_q\sum_{j=0}^{n-k}(-1)^j q^{\binom j2}{n-k\brack j}_q R_q(n-k-j,k,r)R_q(n-k-j,k,s).}
\]
This is an exact nonnegative integer for every prime power \(q\) and every displayed range, with zero terms automatically encoding impossibility.

Summing over the two ranks gives the exact common-kernel distribution
\[
\boxed{\sum_{r,s}C_{n,q}(r,s,k)={n\brack k}_q\prod_{i=0}^{n-k-1}(q^{2k}-q^i).}
\]
Consequently, such a pair exists with common-kernel dimension \(k\) exactly when \(\lceil n/3\rceil\le k\le n\). Summing further over \(k\) gives the entire finite-field representation count
\[
\boxed{N_{n,q}=\sum_{k=\lceil n/3\rceil}^{n}{n\brack k}_q\prod_{i=0}^{n-k-1}(q^{2k}-q^i).}
\]
At fixed \(n\ge2\), as \(q\) tends to infinity through prime powers, the polynomial has degree \(3\lfloor n^2/4\rfloor\) and leading coefficient \(1\) when \(n\) is even, \(2\) when \(n\) is odd. For \(n=1\), the unique pair is the zero pair.

## Assumptions and scope
All matrices act on an \(n\)-dimensional vector space \(V\) over an arbitrary finite field \(\mathbb F_q\); no characteristic restriction is made. The four zero-product conditions are imposed, including the squares, and \(X,Y\) are ordered. The common kernel is the joint annihilator (socle) of the associated representation of the local radical-square-zero two-loop algebra \(\mathbb F_q\langle x,y\rangle/(x,y)^2\). The formula counts actual ordered labeled representations, not similarity classes.

## Proof
Put \(K=\ker X\cap\ker Y\) and write \(\dim K=k\), \(a=n-k\). The four zero-product relations imply \(\operatorname{im}X+\operatorname{im}Y\subseteq K\). Conversely, if \(X\) and \(Y\) kill \(K\) and have image in \(K\), then all four products vanish. For a fixed \(k\)-dimensional subspace \(K\subseteq V\), the pair therefore corresponds uniquely to two linear maps \(f,g:V/K\to K\). Its joint kernel is exactly \(K\) if and only if \(\ker f\cap\ker g=0\). Because \(X\) and \(Y\) vanish on \(K\), their ranks are the ranks of \(f\) and \(g\).

For \(b\)-dimensional source and \(k\)-dimensional target, rank-\(t\) maps are counted by \(R_q(b,k,t)\): choose a \(t\)-dimensional image, a codimension-\(t\) kernel, then an isomorphism between the quotient and image. On the lattice of subspaces of the \(a\)-dimensional source \(U=V/K\), the interval Möbius function is \(\mu(0,W)=(-1)^{\dim W}q^{\binom{\dim W}{2}}\). Applying Möbius inversion to the condition \(\ker f\cap\ker g=0\) gives
\[
\sum_{W\le U}\mu(0,W)\#\{(f,g):\operatorname{rank}f=r,\operatorname{rank}g=s,\ W\subseteq\ker f\cap\ker g\}.
\]
When \(\dim W=j\), both maps factor through \(U/W\), so the cardinality is \(R_q(a-j,k,r)R_q(a-j,k,s)\); there are \({a\brack j}_q\) such subspaces. Multiplying by the \({n\brack k}_q\) possibilities for \(K\) proves the main formula. All possible \(K\) are disjointly partitioned, preventing overcounting.

Without conditioning on individual ranks, the pair \((f,g)\) is equivalent to a single injective map \(U\to K\oplus K\). Such maps number \(\prod_{i=0}^{a-1}(q^{2k}-q^i)\); this proves the marginal and also supplies an independent algebraic derivation. The marginal is nonzero precisely when \(a\le2k\), or \(k\ge\lceil n/3\rceil\). All feasible strata exist since any injection \(U\to K^2\) yields a pair.

Finally, \({n\brack k}_q\) is a monic polynomial of degree \(k(n-k)\) in \(q\). For each feasible \(k\), the injective-map product is monic of degree \(2k(n-k)\); thus the marginal is monic of degree \(3k(n-k)\). When \(n\ge2\), its maximum over feasible \(k\) occurs at \(k=n/2\) for even \(n\), and at the two adjacent integers for odd \(n\ge3\), both feasible. All contributions are nonnegative for prime powers, so their leading terms cannot cancel. This proves the stated degree and leading coefficients.

## Verification
An independently written direct-enumeration checker constructs square-zero matrices over prime fields, performs actual matrix multiplication, computes both matrix ranks and the stacked-map rank (hence common-kernel dimension), and compares every nonempty triple with the formula. Exhaustive instances are \((n,q)=(1,2),(2,2),(2,3),(3,2)\). It also checks the formal rank-marginal identity for \(1\le n\le8\) and \(q\in\{2,3,4,5\}\); for the nonprime orders this latter check uses only the exact integer formulas, not field matrix enumeration. Run `python3 artifacts/verify.py`. Expected terminator: `VERIFY_OK_ANNIHILATING_RANK_STRATA`.

For \((n,q)=(3,2)\) the five nonzero triple strata \((r,s,k):C\) are \((1,1,1):42\), \((0,1,2):21\), \((1,0,2):21\), \((1,1,2):63\), and \((0,0,3):1\), totaling \(148\). The general finite-field assertion is a symbolic proof and is not inferred from finite tests.

## Relationship to prior work
The matrix locus \(X^2=Y^2=XY=YX=0\) is precisely the \((a,b)=(2,2)\) instance of Schröer's variety. Schröer classifies its irreducible components; Morrison previously analyzed components and open orbits of the associated two-loop radical-square-zero representation scheme. Oblak determines which pairs of nilpotent Jordan shapes occur; for square-zero matrices, these are governed by individual ranks. Bleher–Chinburg–Huisgen-Zimmermann give the geometric component structure of local radical-square-zero module varieties, including arbitrary numbers of loops. Bondarenko–Gerasimova–Sergeichuk provide canonical forms for general mutually annihilating operator pairs. These substantial earlier results are not claimed as new.

The present result concerns the exact finite-field cardinality **in each simultaneously prescribed pair of ranks and common-kernel dimension**, and its summed count. The cited classifications describe components, feasible Jordan shapes, or similarity normal forms; they do not state the displayed rational-point multiplicities. Huang later counts all mutually annihilating matrix pairs and all mutually annihilating nilpotent pairs, without the simultaneous square-zero and rank/socle refinement. The stronger surrounding counts therefore do not yield the asserted conditional numbers merely by summation. Earlier geometric parametrizations make the existence of counting formulas plausible, so the originality assessment remains subject to further specialist bibliographic review.

## Limitations
The method applies to pairwise-zero products and does not count arbitrary commuting nilpotents or classify simultaneous similarity orbits. The formulas provide labeled finite-field cardinalities; their numerical evaluation does not independently certify novelty. Exhaustive computational tests are limited to small prime fields, whereas extension fields and arbitrary dimensions are covered by the proof. A historical source may contain an equivalent refined point count under different terminology. Independent mathematical validation has not been performed.

## References
1. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293 (first posted 19 November 2002), Comment. Math. Helv. 79 (2004), 396–426. https://arxiv.org/abs/math/0211293
2. P. Oblak, *Jordan forms for mutually annihilating nilpotent pairs*, arXiv:math/0612300 (12 December 2006), Linear Algebra Appl. 428 (2008), 1476–1491. https://arxiv.org/abs/math/0612300
3. F. M. Bleher, T. Chinburg, B. Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045 (11 July 2014). https://arxiv.org/abs/1407.3045
4. K. Morrison, *The scheme of finite-dimensional representations of an algebra*, Pacific J. Math. 91 (1980), 199–218. https://msp.org/pjm/1980/91-1/pjm-v91-n1-p17-s.pdf
5. V. M. Bondarenko, T. G. Gerasimova, V. V. Sergeichuk, *Pairs of mutually annihilating operators*, arXiv:0812.2155 (11 December 2008), Linear Algebra Appl. 430 (2009), 86–105. https://arxiv.org/abs/0812.2155
6. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (29 October 2021). https://arxiv.org/abs/2110.15566
