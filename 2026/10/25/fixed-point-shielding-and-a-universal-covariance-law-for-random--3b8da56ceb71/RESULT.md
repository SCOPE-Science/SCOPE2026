# Fixed-point shielding and a universal covariance law for random permutation commutators

## Finding

Let \(n\ge3\). Fix any permutation \(\eta\) of \([n]=\{1,\ldots,n\}\), and sample \(\Pi\) uniformly from all permutations of \([n]\). Let \(H=\operatorname{Fix}(\eta)\), \(f=|H|\), and \(g=n-f\). For \(x,j\in[n]\), put
\[
A_x={\bf1}\{\eta(\Pi(x))=\Pi(\eta(x))\},\qquad
B_j={\bf1}\{\Pi(j)=j\},
\]
and write \(C=\sum_{x=1}^n A_x\), \(F=\sum_{j=1}^n B_j\). Then \(C\) is the number of fixed points of the commutator \(\eta^{-1}\Pi^{-1}\eta\Pi\).

**Complete mixed covariance theorem.** For all \(x,j\in[n]\),
\[
\operatorname{Cov}(A_x,B_j)=
\begin{cases}
 g/n^2,&x\in H,\ j=x,\\
 -g/[n^2(n-1)],&x\in H,\ j\in H\setminus\{x\},\\
 f/[n^2(n-1)],&x\in H,\ j\notin H,\\
 f/[n^2(n-1)],&x\notin H,\ j\in\{x,\eta(x)\},\\
 2g/[n^2(n-1)(n-2)],&x\notin H,\ j\in H,\\
 -2f/[n^2(n-1)(n-2)],&x\notin H,\ j\notin H\cup\{x,\eta(x)\}.
\end{cases}
\]
Empty cases are ignored. In particular,
\[
\boxed{\operatorname{Cov}(C,F)=\frac{fg}{(n-1)(n-2)}.}
\]
This aggregate covariance depends on \(\eta\) **only through its number of fixed points**, not its other cycle lengths.

**Sharp pairwise-independence classification.** All \(n^2\) pairs of indicators \((A_x,B_j)\) are independent if and only if \(\eta\) has no fixed points or is the identity. If \(\eta\) is fixed-point-free, this pairwise independence is nondegenerate: \(\Pr(A_x=1)=1/(n-1)\) and \(\Pr(B_j=1)=1/n\) for all indices. Nevertheless the aggregate variables \(C\) and \(F\) are then **not independent**; they are merely uncorrelated. If \(0<f<n\), their covariance is strictly positive.

## Assumptions and scope

The base permutation \(\eta\) is deterministic and arbitrary, including permutations with many cycles, transpositions, fixed points, or no fixed points. The only randomness is an independent uniformly drawn \(\Pi\). Composition is right-to-left; the commutator is defined explicitly as \(\eta^{-1}\Pi^{-1}\eta\Pi\), removing convention ambiguity. The domain is \(n\ge3\) with all \(x,j\in[n]\). No asymptotic or approximation assumption is imposed. The result concerns the exact joint second moments and cross-pair independence; it does not assert mutual independence of either full indicator family.

## Proof

For fixed \(x\in H\), the equality defining \(A_x\) is precisely \(\Pi(x)\in H\), so \(\Pr(A_x=1)=f/n\). For fixed \(x\notin H\), the two values \((\Pi(x),\Pi(\eta(x)))\) form a uniformly sampled ordered distinct pair. Their equality condition is \(\Pi(\eta(x))=\eta(\Pi(x))\). Exactly \(g\) first values lead to a distinct permitted second value, hence
\[
\Pr(A_x=1)=\frac{g}{n(n-1)}\quad(x\notin H).
\]
Also \(\Pr(B_j=1)=1/n\) for every \(j\).

Condition now on \(B_j=1\), which fixes \(\Pi(j)=j\). Write \(h_j={\bf1}\{j\in H\}\). If \(x\in H\), then
\[
\Pr(A_x=1\mid B_j=1)=
\begin{cases}
1,&j=x,\\
(f-h_j)/(n-1),&j\ne x.
\end{cases}
\]
Indeed, away from \(x=j\), the image \(\Pi(x)\) is uniform over the \(n-1\) values other than \(j\).

If \(x\notin H\) and \(j=x\) or \(j=\eta(x)\), one prescribed fixed point forces the other position to be fixed if the commutation equality holds. Thus
\[
\Pr(A_x=1\mid B_j=1)=1/(n-1)
\qquad(j\in\{x,\eta(x)\}).
\]
For \(x\notin H\) and \(j\notin\{x,\eta(x)\}\), choose \(u=\Pi(x)\ne j\). The value at \(\eta(x)\), conditional on \(u\), is uniform over the \(n-2\) values excluding \(j,u\). The equality requires the value \(\eta(u)\), which is feasible exactly when \(\eta(u)\ne u\) and \(\eta(u)\ne j\). There are \(g\) eligible choices of \(u\) if \(j\in H\), and \(g-2\) if \(j\notin H\) (the latter excludes \(j\) and its distinct predecessor \(\eta^{-1}(j)\)). Consequently
\[
\Pr(A_x=1\mid B_j=1)
=\frac{g-2+2h_j}{(n-1)(n-2)}
\quad(j\notin\{x,\eta(x)\}).
\]
Every feasible conditional probability above is well-defined because \(n\ge3\), and cases with no applicable indices require no evaluation.

Since \(\Pr(B_j=1)=1/n\), the identity
\[
\operatorname{Cov}(A_x,B_j)
=\frac1n\left[\Pr(A_x=1\mid B_j=1)-\Pr(A_x=1)\right]
\]
gives all six displayed cross-covariance cases by elementary subtraction. As an internal check, the row sums are
\[
\sum_j\operatorname{Cov}(A_x,B_j)=
\begin{cases}
 g/[n(n-1)],&x\in H,\\
 2f/[n(n-1)(n-2)],&x\notin H.
\end{cases}
\]
There are \(f\) rows of the first kind and \(g\) of the second. Summing yields
\[
\operatorname{Cov}(C,F)=
\frac{fg}{n(n-1)}+\frac{2fg}{n(n-1)(n-2)}
=\frac{fg}{(n-1)(n-2)}.
\]

If \(f=0\), then for every \(x,j\), \(\Pr(A_x=1\mid B_j=1)=1/(n-1)=\Pr(A_x=1)\), so \(A_x\) and \(B_j\) are independent Bernoulli variables. If \(f=n\), \(A_x\equiv1\), giving trivial independence. Conversely, if \(0<f<n\), choose \(x\in H\) and \(j=x\): their covariance \(g/n^2\) is strictly positive, so not all pairs are independent.

Finally take \(f=0\). Then \(\eta\ne\mathrm{id}\); since the center of the symmetric group on at least three points is trivial, there is a permutation \(\pi\) not commuting with \(\eta\). Hence \(C\) is not identically \(n\), whereas \(F=n\) occurs with probability \(1/n!>0\) and forces \(\Pi=\mathrm{id}\), hence \(C=n\). Thus \(C\) and \(F\) are not independent, despite their zero covariance. This also follows constructively from a noncommuting transposition.

## Verification

The accompanying `verify_commutator.py` enumerates all \(\eta\) and \(\Pi\) for dimensions \(3,4,5\), and samples distinct representative \(\eta\) at dimension \(6\). It computes cross-covariances from full enumerations of \(\Pi\), checks each of the six formulas using exact rational fractions, verifies the aggregate covariance, and tests the pairwise-independence characterization. The unrestricted theorem is proved above by counting, not inferred from finite enumeration. Run with `python verify_commutator.py` using Python 3 standard library only.

## Relationship to prior work

Diaconis, Evans and Graham, *Unseparated pairs and fixed points in random permutations* (arXiv:1308.5459, first submitted 2013-08-25), study the marginal commutator fixed-point law. Their Section 6 gives the mean and Poisson approximation based on \(\operatorname{Fix}(\eta)\) and two-cycles. The present statement is a **mixed, same-permutation** law, with \(B_j\) dependent on the very \(\Pi\) forming the commutator; it is not recovered by independently sampling the conjugates used for marginal analysis. No result stating the displayed cross-covariance matrix, its \(f\)-only aggregate reduction, or the all-pairs independence criterion was found in that article's relevant full-text sections.

Diaconis, Fulman and Guralnick, *On fixed points of permutations* (arXiv:0708.2643, submitted 2007-08-20), develop general fixed-point statistics of permutation group actions. Their fixed-point formulas do not directly address covariance with the original permutation's fixed-point count when the tested observable itself depends on a deterministic commutator partner.

Related exact fixed-point/linear-succession cross-covariance work concerns events \(\Pi(i+1)=\Pi(i)+1\) without cyclic wrap-around. This differs from pointwise commutation with an arbitrary \(\eta\); even when \(\eta\) is an \(n\)-cycle, the present cyclic equality differs at both the position and value boundaries and exhibits exact pairwise independence absent in the linear case.

## Limitations

This is a second-order dependence classification and an all-pairs (not all-events) independence theorem. In particular, zero covariance of \(C\) and \(F\) when \(\eta\) has no fixed points does **not** imply their independence; the proof establishes the opposite. It does not derive a full bivariate generating function or quantitative convergence rates. The historically closest commutator literature was inspected, but possible earlier implicit derivations via general representation-theoretic mixed-moment identities remain a priority risk. Independent historical-priority and proof assessments have not been carried out.

## References

1. P. Diaconis, S. N. Evans, and R. L. Graham, *Unseparated pairs and fixed points in random permutations*, arXiv:1308.5459, submitted 2013-08-25; *Advances in Applied Mathematics* **61** (2014), 102–124. https://arxiv.org/abs/1308.5459 ; freely accessible authors' full text: https://mathweb.ucsd.edu/~ronspubs/14_05_pairs.pdf
2. P. Diaconis, J. Fulman, and R. Guralnick, *On fixed points of permutations*, arXiv:0708.2643, submitted 2007-08-20. https://arxiv.org/abs/0708.2643
