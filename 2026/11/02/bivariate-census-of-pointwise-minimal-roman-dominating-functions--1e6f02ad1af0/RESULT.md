# Bivariate census of pointwise-minimal Roman dominating functions on cycles

## Finding
For every integer \(n\geq 3\), let \(C_n\) be the labeled cycle with vertices \(0,\ldots,n-1\). A Roman dominating function is a map \(f:V(C_n)\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\). It is *pointwise-minimal* if no distinct Roman dominating function is coordinatewise at most \(f\). Write \(k(f)=|f^{-1}(2)|\) and \(w(f)=\sum_v f(v)\), and form the bivariate polynomial
\[
R_n(y,z)=\sum_{f\text{ pointwise-minimal}}y^{k(f)}z^{w(f)}.
\]
Define the polynomial
\[
D(x,y,z)=1-zx-yz^2x^3-y^2z^4x^4-y^2z^4x^5.
\]
Then the **complete census for all numbers of double-guard vertices and all weights** is
\[
\boxed{R_n(y,z)=[x^n]\left(-\frac{x\,\partial D(x,y,z)/\partial x}{D(x,y,z)}\right)\qquad(n\ge3).}
\]
Equivalently,
\[
\sum_{n\ge3}R_n(y,z)x^n=-\frac{xD_x(x,y,z)}{D(x,y,z)}-zx-z^2x^2.
\]
The coefficients obey, for \(n\ge6\),
\[
R_n=zR_{n-1}+yz^2R_{n-3}+y^2z^4R_{n-4}+y^2z^4R_{n-5}.
\]
The initial polynomials are
\[
\begin{aligned}
R_3&=z^3+3yz^2,\\
R_4&=z^4+4yz^3+4y^2z^4,\\
R_5&=z^5+5yz^4+5y^2z^4+5y^2z^5.
\end{aligned}
\]
The recurrence formally uses \(R_1=z\) and \(R_2=z^2\); these two seeds are algebraic conventions, not claims about simple cycles of order one or two.

As a consequence, if \(c_n=R_n(1,1)\), then
\[
c_3,c_4,\ldots,c_{12}=4,9,16,22,36,65,112,186,309,522,
\]
and \(c_n=c_{n-1}+c_{n-3}+c_{n-4}+c_{n-5}\) for \(n\ge6\). Moreover,
\[
c_n=\lambda^n+O(\rho^n),\qquad 0<\rho<\lambda,
\]
where \(\lambda=1.685137110\ldots\) is the unique positive root of
\[
\lambda^5-\lambda^4-\lambda^2-\lambda-1=0.
\]
The leading asymptotic coefficient is exactly one. The numerical recurrence by itself is not asserted to be a newly discovered integer sequence: an identical unlabeled sequence and rational generating function appear in Plouffe's table of Fielder sequences (1992, entry A1639). The new assertion is its cycle-minimal-Roman interpretation and the two-variable classification and enumerator.

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled. The domain is exactly \(n\in\mathbb Z\) with \(n\ge3\). Pointwise minimality refers to the partial order induced by \(0<1<2\) independently at every vertex; it does not mean minimum total weight. A polynomial's monomial \(y^kz^w\) counts labeled functions with exactly \(k\) labels equal to \(2\) and total weight \(w\). All generating series are formal power series in \(x\), with polynomial coefficients in \(y,z\).

## Proof
**Step 1: intrinsic minimality.** Fix a subset \(A\subseteq V(C_n)\), intended as the vertices labeled \(2\). In a pointwise-minimal Roman dominating function, each neighbor of \(A\) outside \(A\) must carry label \(0\), since lowering a label \(1\) there to \(0\) would preserve Roman domination. Conversely, all vertices outside the closed neighborhood of \(A\) must carry label \(1\). Thus \(A\) uniquely determines a candidate function, with label \(2\) on \(A\), label \(0\) on \(N(A)\setminus A\), and label \(1\) elsewhere. This function is minimal if and only if every \(a\in A\) has a neighbor \(u\notin A\) whose only neighbor in \(A\) is \(a\): such a private zero-vertex prevents lowering the label at \(a\) from \(2\) to \(1\). If it does not exist, the label at \(a\) can be lowered to \(1\) without losing Roman domination. The other possible single-coordinate decreases already fail. Since Roman domination is upward-closed in the coordinatewise order, ruling out all single-coordinate decreases is equivalent to pointwise minimality. The empty set \(A\) yields the all-one function.

**Step 2: cyclic gaps.** Suppose \(A\ne\emptyset\) has \(t\) vertices. Write the successive numbers of nonselected vertices between consecutive elements of \(A\) as \(g_1,\ldots,g_t\ge0\), indexed cyclically, so \(n=t+\sum_j g_j\). A selected vertex has a private zero-vertex on its left exactly when the preceding gap is at least two, and on its right exactly when the following gap is at least two. Hence the candidate is minimal if and only if **no two cyclically consecutive gaps belong to \(\{0,1\}\)**. This includes \(t=1\), for which its sole gap must have length at least two, and \(t=2\), for which the two gaps cannot both be short. A gap of length \(g\) contributes \(\max(g-2,0)\) to the total label weight from vertices labeled \(1\). Therefore
\[
w(f)=2t+\sum_{j=1}^t\max(g_j-2,0).
\]

**Step 3: exact cyclic enumeration.** Mark the contribution from a single gap including its initial selected vertex by \(x\) for each occupied graph position, \(y\) for each selected vertex, and \(z\) for each unit of total weight. The short-gap and long-gap series are respectively
\[
S(x,y,z)=yz^2(x+x^2),\qquad L(x,y,z)=\frac{yx^3z^2}{1-xz}.
\]
An ordered cyclic sequence of \(t\) gaps has no adjacent short gaps if and only if it is a closed walk of length \(t\) in the weighted matrix
\[
M=\begin{pmatrix}L&S\\L&0\end{pmatrix}.
\]
Thus \(\operatorname{tr}(M^t)\) enumerates the legal ordered sequences. For every such sequence and each choice of a root index among the \(n\) labeled cycle positions we obtain a selected set with a distinguished selected vertex; conversely each selected set with \(t\) elements is counted exactly \(t\) times. Consequently the nonempty selected-set contribution to \(R_n\) equals
\[
n[x^n]\sum_{t\ge1}\frac{\operatorname{tr}(M^t)}{t}.
\]
Using the formal identity \(\sum_{t\ge1}\operatorname{tr}(M^t)/t=-\log\det(I-M)\), one obtains
\[
\det(I-M)=1-L-LS=\frac{D(x,y,z)}{1-xz}.
\]
Adding the all-one contribution \(z^n\) gives
\[
R_n=z^n+n[x^n]\log\frac{1-xz}{D(x,y,z)}.
\]
Finally \(n[x^n]H(x)=[x^n]xH'(x)\). The derivative of \(\log(1-xz)\) contributes \(-z^n\), cancelling the all-one term, and yielding the claimed logarithmic-derivative formula. Coefficient comparison against \(D\) establishes the initial polynomials and the recurrence.

**Step 4: asymptotic.** At \(y=z=1\), put \(d(x)=1-x-x^3-x^4-x^5\). It has a unique root \(\alpha\) of smallest modulus, which is real and positive: for \(|x|<\alpha\), \(|x+x^3+x^4+x^5|<1\); equality on \(|x|=\alpha\) forces all four positive monomials to share phase, and the exponents \(1,3,4,5\) force \(x=\alpha\). The root is simple since \(d'(\alpha)<0\). Therefore \(-xd'(x)/d(x)\) has principal part \(1/(1-x/\alpha)\) near \(\alpha\), and all other poles are farther from the origin. Coefficient extraction yields \(c_n=\alpha^{-n}+O(\rho^n)\) for some \(\rho<\alpha^{-1}\), proving the assertion with \(\lambda=\alpha^{-1}\).

## Verification
The standalone `verify.py` uses only the Python standard library. It generates the polynomial coefficients by the displayed rational recurrence and independently enumerates all \(3^n\) possible labelings for every \(3\le n\le12\). A labeling is judged by the original Roman condition and, independently of the gap theorem, by attempting every possible single-coordinate lowering. It compares the complete bivariate coefficient dictionaries, not merely their totals. A second enumeration tests every selected-vertex subset for \(3\le n\le17\) against the private-neighbor gap condition and compares complete bivariate distributions. Execution returned `VERIFY_OK`. These are finite consistency checks; the unbounded theorem is proved by the gap and generating-function argument above.

## Relationship to prior work
Abu-Khzam, Fernau, and Mann (arXiv:2204.04765, first posted 2022-04-10) introduced efficient enumeration of pointwise-minimal Roman dominating functions and characterized the allowed sets of vertices labeled \(2\). Their Proposition 10 explicitly counts the \(16\) minimal functions of \(C_5\), a base case recovered here. Abu-Khzam, Fernau, and Mann (arXiv:2208.05261, first posted 2022-08-10), Section 4, derive a recursive count for paths, while Section 9 identifies extensions to other simple graph classes as future work. Neither inspected treatment provides the all-cycle bivariate polynomial or the cyclic-gap determinant. Plouffe's 1992 table (Appendix A, page A.178, entry A1639) gives the same *univariate sequence* as a Fielder sequence and its rational generating function, without a Roman domination interpretation or the \(y,z\)-weighted refinement; the mere numerical recurrence is thus explicitly excluded from the novelty claim. Standard domination polynomials count dominating vertex subsets, not pointwise-minimal Roman functions.

## Limitations
This is an exact theorem only for ordinary pointwise-minimal Roman dominating functions on simple labeled cycles. It is not a formula for weight-minimizing Roman functions alone, not a theorem for all unicyclic graphs, and not a claim of new numerical coefficients at \(y=z=1\) divorced from their graph interpretation. The proof is mathematical rather than computationally certified; independent mathematical audit is not yet performed. The literature search cannot exclude unindexed or inaccessible equivalent prior work, and the old Fielder-sequence match creates an explicit priority qualification for the univariate specialization.

## References
1. F. N. Abu-Khzam, H. Fernau, K. Mann, *Minimal Roman Dominating Functions: Extensions and Enumeration*, arXiv:2204.04765 (first public version, 2022-04-10). https://arxiv.org/abs/2204.04765
2. F. N. Abu-Khzam, H. Fernau, K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes*, arXiv:2208.05261 (first public version, 2022-08-10). https://arxiv.org/abs/2208.05261
3. S. Plouffe, *Approximations de séries génératrices et quelques conjectures*, Université du Québec à Montréal, 1992, Appendix A, entry A1639 (Fielder sequence). https://oeis.org/A000051/a000051_2.pdf
