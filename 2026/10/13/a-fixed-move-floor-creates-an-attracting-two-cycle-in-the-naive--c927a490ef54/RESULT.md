# A fixed move floor creates an attracting two-cycle in the Naive Separation Algorithm

## Finding
For Algorithm 2 (Naive Separation Algorithm) in Matsuno (2026), fix \(\eta=1/10\) and any stopping tolerance \(\varepsilon>0\). Let \(P=\{A,B,C\}\) with \(A=(1,-50)\), \(B=(1,-5)\), \(C=(2,50)\), and initialize \(x_0=B\). Then \(0\notin \operatorname{conv}(P)\), but the algorithm never terminates: it alternately selects \(C\) and \(A\), its clipped coefficient is \(\alpha_k=9/10\) for every \(k\), and the even and odd subsequences converge to the attracting two-cycle \(x_-^*=(28/19,-50/19)\), \(x_+^*=(29/19,50/19)\) with exact two-step factor \(81/100\). Consequently, the fixed-support-face assumption used in the paper's Theorem 3.2 is not implied by Algorithm 2, and the cap \(\alpha_k\le 1-\eta\) can prevent convergence to a separating normal even when the polytope is strictly separated from the origin.

## Assumptions and scope
The source algorithm takes a finite vertex set \(P\) with \(0\notin \operatorname{conv}(P)\), a tolerance \(\varepsilon>0\), and \(\eta\in(0,1)\). At iterate \(x_k\), it sets \(h_k=x_k/\|x_k\|\), chooses a vertex minimizing \(h_k^\top p\), forms
\[
\theta_k=\frac{p_k^\top(p_k-x_k)}{\|p_k-x_k\|^2},\qquad
\alpha_k=\min\{\max\{\theta_k,0\},1-\eta\},
\]
and updates \(x_{k+1}=\alpha_kx_k+(1-\alpha_k)p_k\). The stopping test requires the selected minimum \(h_k^\top p_k\) to exceed \(\varepsilon\).

The counterexample fixes \(\eta=1/10\), allows every \(\varepsilon>0\), and uses the three non-collinear vertices \(A=(1,-50)\), \(B=(1,-5)\), and \(C=(2,50)\). Since every point of their convex hull has first coordinate at least \(1\), the origin is strictly outside the hull. The initialization \(x_0=B\) is one of the initializations allowed by Algorithm 2.

## Proof
Because \(h_k\) is a positive scalar multiple of \(x_k\), the minimizing vertex is also the minimizer of \(x_k^\top p\). Define the two rectangles
\[
R_-=[1,2]\times[-5,-50/19],\qquad
R_+=[1,2]\times[1/2,50/19].
\]
The start \(x_0=B\) lies in \(R_-\).

Take \(x=(u,v)\in R_-\). Then
\[
x^\top(C-B)=u+55v<0,\qquad x^\top(C-A)=u+100v<0,
\]
so \(C\) is the unique minimizing vertex. Put \(a=2-u\in[0,1]\) and \(b=50-v\in[1000/19,55]\). The unclipped coefficient for \(C\) is
\[
\theta_C=\frac{2a+50b}{a^2+b^2}.
\]
Its excess above \(9/10\) has numerator
\[
2a+50b-\frac9{10}(a^2+b^2)
=a\left(2-\frac9{10}a\right)+b\left(50-\frac9{10}b\right)>0,
\]
because \(a\le1\) and \(b\le55\). Hence \(\alpha=9/10\), and
\[
T_C(u,v)=\left(\frac9{10}u+\frac15,\frac9{10}v+5\right)\in R_+.
\]
Moreover, the selected stopping quantity is negative:
\[
x^\top C=2u+50v\le4-\frac{2500}{19}<0.
\]

Now take \(x=(u,v)\in R_+\). Since \(v>0\),
\[
x^\top(A-B)=-45v<0,\qquad x^\top(A-C)=-u-100v<0,
\]
so \(A\) is the unique minimizing vertex. Put \(a=u-1\in[0,1]\) and \(b=50+v\in[101/2,1000/19]\). The unclipped coefficient is
\[
\theta_A=\frac{50b-a}{a^2+b^2}.
\]
For its excess above \(9/10\),
\[
50b-a-\frac9{10}(a^2+b^2)
=b\left(50-\frac9{10}b\right)-a-\frac9{10}a^2.
\]
The first term is at least \(50000/361\), while the magnitude of the last two terms is at most \(19/10\), so the expression is positive. Thus \(\alpha=9/10\), and
\[
T_A(u,v)=\left(\frac9{10}u+\frac1{10},\frac9{10}v-5\right)\in R_-.
\]
Again the selected stopping quantity is negative:
\[
x^\top A=u-50v\le2-25<0.
\]
Therefore the algorithm alternates forever between \(R_-\) and \(R_+\), with the unique selected vertices \(C,A,C,A,\ldots\), coefficient \(9/10\) at every step, and no stopping test can succeed for any \(\varepsilon>0\).

The two-step map on \(R_-\) is
\[
T_A\!\circ T_C(x)=\frac{81}{100}x+\frac9{100}C+\frac1{10}A.
\]
It has the unique fixed point
\[
x_-^*=\left(\frac{28}{19},-\frac{50}{19}\right),
\]
and its positive partner is
\[
x_+^*=T_C(x_-^*)=\left(\frac{29}{19},\frac{50}{19}\right).
\]
Hence
\[
x_{2m}-x_-^*=\left(\frac{81}{100}\right)^m(x_0-x_-^*),
\]
and the analogous formula holds for the odd subsequence relative to \(x_+^*\). This proves attraction to a nontrivial period-two orbit.

## Verification
The accompanying verifier uses exact rational arithmetic. It checks the initial unique minimizer, the clipping inequality, the rectangle invariance inequalities, the two affine maps, the exact two-cycle, and the two-step contraction factor. Running the verifier returns `VERIFY_OK`.

The proof is analytic: the finite arithmetic checks confirm exact identities and boundary inequalities, while the infinite nontermination conclusion follows from the proved forward invariance of \(R_-\cup R_+\), not from finite iteration sampling.

## Relationship to prior work
Matsuno's 2026 article defines this Naive Separation Algorithm and states its convergence theorem under an additional assumption that every selected vertex lies on one fixed supporting face associated with a fixed normal. The construction above shows that this assumption is not generated automatically by Algorithm 2: the selected vertex alternates between two distinct vertices forever. The article itself does not give this triangle, this invariant-region argument, or this period-two limit.

The original LP-Newton literature and the simple-projection variant use minimum-norm projections or binary-search structure rather than the clipped exact-line-search rule above. The 2025 finite-termination LP-Newton variant is explicitly a different replacement for Wolfe's minimum-norm routine. Standard Frank--Wolfe terminology gives an equivalent interpretation of the NSA update on the objective \(\|x\|^2/2\): the cap \(\alpha_k\le1-\eta\) imposes a move weight of at least \(\eta\) toward the linear-minimization vertex. Searches for fixed-step, fixed-minimum-step, periodic-orbit, minimum-norm, and separating-hyperplane formulations did not locate a prior statement that implies this exact source-specific triangle counterexample.

## Limitations
The result is a counterexample for one admissible parameter value and one allowed initialization; it does not classify all \(\eta\), all triangles, or all initializations. It does not contradict Theorem 3.2 under that theorem's additional fixed-support-face hypothesis. It shows instead that Algorithm 2 by itself does not ensure that hypothesis or unconditional convergence. Broader fixed-step conditional-gradient phenomena are related, so the originality claim is limited to this exact algorithmic boundary result and its explicit invariant two-cycle, not to the general observation that nonvanishing step sizes can oscillate.

## References
1. Y. Matsuno, “A numerical LP-Newton method for solving linear programming using separating hyperplanes,” AIMS Mathematics 11(2), 4691–4704 (2026). DOI: 10.3934/math.2026191.
2. S. Fujishige, T. Hayashi, K. Yamashita, and U. Zimmermann, “Zonotopes and the LP-Newton method,” Optimization and Engineering 10, 193–205 (2009). DOI: 10.1007/s11081-008-9067-x.
3. T. Kitahara and N. Sukegawa, “A simple projection algorithm for linear programming problems,” Algorithmica 81, 167–178 (2019). DOI: 10.1007/s00453-018-0436-3.
4. Y. Matsuno and J. Shi, “Rethinking linear programming: A new finite-termination LP-Newton approach,” Lecture Notes in Networks and Systems 1311, 76–82 (2025). DOI: 10.1007/978-3-031-90606-0_7.
5. J. A. De Loera, J. Haddock, and L. Rademacher, “The minimum Euclidean-norm point in a convex polytope: Wolfe's combinatorial algorithm is exponential,” SIAM Journal on Computing 49, 138–169 (2020). DOI: 10.1137/18M1221072.
