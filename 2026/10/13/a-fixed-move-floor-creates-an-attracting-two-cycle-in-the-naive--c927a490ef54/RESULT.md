# A fixed move floor creates an attracting two-cycle in the Naive Separation Algorithm

## Finding
In Matsuno's Naive Separation Algorithm (Algorithm 2), take \(\eta=1/10\), any stopping tolerance \(\varepsilon>0\), and the vertices \(A=(1,-50)\), \(B=(1,-5)\), and \(C=(2,50)\). Initialize \(x_0=B\). The origin is strictly outside the convex hull, but the algorithm never terminates. The unique selected vertices alternate \(C,A,C,A,\ldots\), the clipped coefficient remains \(9/10\), and the iterates converge by parity to an attracting period-two orbit
\[
x_-^*=\left(\frac{28}{19},-\frac{50}{19}\right),\qquad
x_+^*=\left(\frac{29}{19},\frac{50}{19}\right)
\]
with exact two-step contraction factor \(81/100\). Neither limiting normal separates the origin from the triangle. This proves that the fixed move floor can cause nontermination under the inputs of Algorithm 2 even on a strictly separated triangle.

The example satisfies Theorem 3.2's stated fixed-support-face premise: the common minimizing face is \(AC\), with a **negative** support value. Its distance quantity tends to zero as the theorem asserts, but this does not imply termination or convergence to a separating normal.

## Assumptions and scope
For \(P=\{A,B,C\}\), Algorithm 2 starts at an arbitrary vertex and uses \(h_k=x_k/\|x_k\|\). It selects a minimizer \(p_k\) of \(h_k^\top p\) over \(P\), terminates if \(h_k^\top p_k>\varepsilon\), and otherwise uses
\[
\theta_k=\frac{p_k^\top(p_k-x_k)}{\|p_k-x_k\|^2},\qquad
\alpha_k=\min\{\max\{\theta_k,0\},1-\eta\},\qquad
x_{k+1}=\alpha_k x_k+(1-\alpha_k)p_k.
\]
The floor \(1-\alpha_k\ge\eta\) is on the weight of the newly selected vertex. Every point of \(\operatorname{conv}(P)\) has first coordinate at least one, so \((1,0)\) gives a strictly positive separating margin and every iterate is nonzero. The updates below always have \(p_k\ne x_k\), so the coefficient is defined.

## Proof
The minimizing vertex for \(h_k\) is the same as for \(x_k\). Use
\[
R_-=[1,2]\times[-5,-50/19],\qquad R_+=[1,2]\times[1/2,50/19].
\]
The start lies in \(R_-\). There, writing \(x=(u,v)\), one has \(x^\top(C-B)=u+55v<0\) and \(x^\top(C-A)=u+100v<0\). Thus \(C\) is uniquely selected. Set \(a=2-u\in[0,1]\) and \(b=50-v\in[1000/19,55]\). The numerator of \(\theta_C-9/10\) over \(a^2+b^2\) is
\[
a(2-9a/10)+b(50-9b/10)>0;
\]
the first term is nonnegative and the second positive since \(b\le55\). Consequently \(\alpha=9/10\). The selected dot product is \(x^\top C\le4-2500/19<0\). The step is \(T_C(u,v)=(9u/10+1/5,9v/10+5)\); it maps the first coordinate into \([1,2]\) and the endpoints of the second-coordinate interval to \(1/2\) and \(50/19\), so it maps \(R_-\) into \(R_+\).

On \(R_+\), \(x^\top(A-B)=-45v<0\) and \(x^\top(A-C)=-u-100v<0\), so \(A\) is uniquely selected. Now let \(a=u-1\in[0,1]\) and \(b=50+v\in[101/2,1000/19]\). The numerator of \(\theta_A-9/10\) over \(a^2+b^2\) is
\[
b(50-9b/10)-a-9a^2/10\ge 50000/361-19/10>0.
\]
Here \(b(50-9b/10)\) is decreasing over this range, and the bound uses its value at \(1000/19\). The selected dot product is \(x^\top A\le2-25<0\). The clipped map \(T_A(u,v)=(9u/10+1/10,9v/10-5)\) maps the first coordinate into \([1,2]\); the second-coordinate endpoints map to \(-91/20\) and \(-50/19\), within \([-5,-50/19]\). Thus \(T_A(R_+)\subset R_-\).

Induction gives perpetual alternation, cap activation, and a strictly negative selected dot product. Normalization leaves its sign unchanged, so no stopping test can succeed. The two-step map on \(R_-\) is \(T_A T_C(x)=(81/100)x+(9/100)C+(1/10)A\). Its unique fixed point is the stated \(x_-^*\); applying \(T_C\) gives \(x_+^*\). It follows that \(x_{2m}-x_-^*=(81/100)^m(x_0-x_-^*)\), and likewise \(x_{2m+1}-x_+^*=(81/100)^m(x_1-x_+^*)\). The strict selection, clipping, and stopping inequalities also hold on neighborhoods of the two orbit points by continuity; sufficiently small equal-radius balls about them are sent into each other because each affine map contracts by \(9/10\). This gives local attraction as well as convergence from the assigned start.

## Relation to Theorem 3.2
For the normal \(n=(-100,1)\), \(n^\top A=n^\top C=-150\) and \(n^\top B=-105\); hence \(AC\) is the minimizing face. The quantity \(d_k=n^\top x_k+150\) starts at \(45\), and the update with either selected vertex gives \(d_{k+1}=(9/10)d_k\). If a unit normal is used these quantities are divided by \(\sqrt{10001}\). This is precisely the face-distance behavior in Theorem 3.2. A nonzero normal constant on \(AC\) must be proportional to \(n\); its minimizing orientation on \(AC\) has negative support. Reversing it selects \(B\), not \(AC\). Thus the selected face is not a positive-support separating face. The construction neither violates the printed premise of Theorem 3.2 nor contradicts its scalar convergence conclusion.

## Verification
The accompanying `verify_counterexample.py` checks the rational clipping inequalities, invariant-region bounds and cycle identities. It does not address the source theorem's scope. Infinite nontermination and the distinction between approaching a face and finding a separating normal follow from the analytic proof, not from finitely many iterates.

## Relationship to prior work and limitations
Matsuno defines the clipped update and proves conditional decay of a distance quantity. That result does not give the nonterminating trajectory, its rational orbit or its contraction factor, and the present example does not purport to refute it. For the objective \(\|x\|^2/2\), the update is a conditional-gradient segment minimization with a lower bound on the move weight. Qualitative oscillation under nonvanishing steps is not the claim of originality. The specific contribution is an exact example for the printed algorithm with an allowed start, a uniform sign obstruction to termination for every positive tolerance, and a computable attracting orbit despite strict separation. Earlier projection and minimum-norm variants address related but different update maps. The result does not classify other parameters, triangles or starting points; equivalent examples in less-indexed fixed-step literature are not ruled out.

## References
1. Y. Matsuno, “A numerical LP-Newton method for solving linear programming using separating hyperplanes,” *AIMS Mathematics* 11(2), 4691–4704 (2026), DOI: [10.3934/math.2026191](https://doi.org/10.3934/math.2026191), Algorithm 2 and Theorem 3.2, p. 4696.
2. S. Fujishige, T. Hayashi, K. Yamashita, and U. Zimmermann, “Zonotopes and the LP-Newton method,” *Optimization and Engineering* 10, 193–205 (2009), DOI: 10.1007/s11081-008-9067-x.
3. T. Kitahara and N. Sukegawa, “A simple projection algorithm for linear programming problems,” *Algorithmica* 81, 167–178 (2019), DOI: 10.1007/s00453-018-0436-3.
4. Y. Matsuno and J. Shi, “Rethinking linear programming: A new finite-termination LP-Newton approach,” *Lecture Notes in Networks and Systems* 1311, 76–82 (2025), DOI: 10.1007/978-3-031-90606-0_7.
5. J. A. De Loera, J. Haddock, and L. Rademacher, “The minimum Euclidean-norm point in a convex polytope: Wolfe's combinatorial algorithm is exponential,” *SIAM Journal on Computing* 49, 138–169 (2020), DOI: 10.1137/18M1221072.
