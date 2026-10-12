# A characteristic split in the exact two-copy quadratic hidden-polynomial success probability
## Finding
For the degree-two two-copy approximative measurement considered by Decker--Draisma--Wocjan, let \(\mathbb F_q\) be a finite field and use their quadratic good set
\[
X_{\rm good}=\{(x,y)\in\mathbb F_q^2:xy(x+y)\ne0\}.
\]
For \((x,y)\in X_{\rm good}\), define \(\eta^{x,y}_{v,w}\) as the number of \((b,c)\in\mathbb F_q^2\) satisfying
\[
xb+yc=v,\qquad xb^2+yc^2=w.
\]
Then the success probability of the source's approximative measurement is exactly
\[
P_q=
\begin{cases}
\displaystyle \frac{(q-1)(q-2)}{q^2}, & \operatorname{char}(\mathbb F_q)=2,\ q\ge4,\\[6pt]
\displaystyle \frac{(q-1)(q-2)}{q^4}\left(1+\frac{q-1}{\sqrt2}\right)^2, & \operatorname{char}(\mathbb F_q)\ne2.
\end{cases}
\]
Thus
\[
P_q\longrightarrow1
\]
along fields of characteristic two, whereas
\[
P_q\longrightarrow\frac12
\]
along odd-characteristic fields.  The same quadratic measurement therefore has two different sharp large-field success plateaus.

## Assumptions and scope
The statement concerns the two-copy, degree-two approximative measurement and the good set specified by Example 4.7 of arXiv:0706.1219.  The field size satisfies \(q\ge3\); in characteristic two this means \(q\ge4\).  No claim is made about optimal state discrimination, the ideal measurement outside the source's good set, higher polynomial degrees, or the later algorithms based on hidden-symmetry reductions or phase linearization.

For the source's Eq. (16), degree two gives
\[
P_q=\frac1{q^6}\sum_{(x,y)\in X_{\rm good}}
\left(\sum_{(v,w):\eta^{x,y}_{v,w}>0}\sqrt{\eta^{x,y}_{v,w}}\right)^2.
\]
Example 4.7 has the auxiliary polynomial \(h(x,y,v,w)=xy(x+y)^2\), independent of \((v,w)\), so for every good \((x,y)\) the allowed output set is exactly the set of nonempty fibers.

## Proof
Fix \((x,y)\in X_{\rm good}\) and put \(s=x+y\).  For any solution \((b,c)\), direct expansion gives the weighted-variance identity
\[
sw-v^2
=(x+y)(xb^2+yc^2)-(xb+yc)^2
=xy(b-c)^2.
\]
Because \(x\), \(y\), and \(s\) are nonzero, for fixed \(v\) the quantity
\[
R=\frac{sw-v^2}{xy}
\]
runs bijectively through \(\mathbb F_q\) as \(w\) runs through \(\mathbb F_q\).

Suppose first that the characteristic is odd.  If \(R=0\), then \(b-c=0\), and the linear equation \(xb+yc=v\) gives one solution.  If \(R\) is a nonzero square, there are exactly two choices \(b-c=\pm\sqrt R\), and each choice gives exactly one pair
\[
b=\frac{v+y(b-c)}s,\qquad c=\frac{v-x(b-c)}s.
\]
If \(R\) is a nonsquare there is no solution.  For each fixed \(v\), exactly one value of \(w\) has a one-point fiber and exactly \((q-1)/2\) values have a two-point fiber.  Varying \(v\) therefore gives
\[
\#\{(v,w):\eta=1\}=q,
\qquad
\#\{(v,w):\eta=2\}=\frac{q(q-1)}2.
\]
Hence the inner sum is
\[
q+\frac{q(q-1)}2\sqrt2
=q\left(1+\frac{q-1}{\sqrt2}\right).
\]

In characteristic two, subtraction and addition agree and the Frobenius map \(z\mapsto z^2\) is a bijection of every finite field.  Thus the identity determines a unique value of \(b-c\) for every \((v,w)\), after which the nonzero coefficient \(s\) determines a unique \((b,c)\).  Therefore all \(q^2\) fibers are singletons and the inner sum equals \(q^2\).

Finally,
\[
|X_{\rm good}|=(q-1)(q-2),
\]
since \(x\ne0\) and, for each such \(x\), the value \(y\) can be any nonzero element except \(-x\).  Substitution into Eq. (16) yields the two displayed formulas.  Their limits are immediate.

## Verification
The proof is symbolic and does not depend on finite enumeration.  The accompanying `verify.py` independently reconstructs every generic fiber for the odd prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13}\), the odd extension field \(\mathbb F_9\), and the characteristic-two fields \(\mathbb F_4,\mathbb F_8,\mathbb F_{16}\).  It checks the fiber-size distributions and the closed success formulas exactly up to floating-point evaluation of the final square-root expression.  The computation is supplementary; the proof above establishes the result for all finite fields in the stated range.

## Relationship to prior work
The prime-field predecessor arXiv:quant-ph/0703195 writes the same quadratic fiber equations, observes that generic fibers have one or two solutions, and obtains the lower bound \(1/4-O(1/p)\) by replacing every nonempty-fiber contribution by one.  It does not count the one-point and two-point fibers separately and does not give the exact success probability.

The later treatment arXiv:0706.1219 formulates the approximative measurement in Eq. (16), proves a field-size-independent lower bound, and in Example 4.7 identifies \(xy(x+y)^2\) as the quadratic good-set polynomial.  That example specifically makes the method available in characteristic two but does not state the exact characteristic-dependent success law above.

arXiv:1107.2189 replaces the earlier route by hidden-symmetry subgroup reductions, and arXiv:1305.1543 introduces phase linearization, including a different odd-field quadratic construction.  Those later algorithms establish efficient solvability under broader conditions but do not determine the success probability of the 2007 two-copy approximative measurement.

## Limitations
The result quantifies one published measurement scheme; it is not an optimality theorem.  The characteristic-two branch starts at \(q=4\), since \(X_{\rm good}\) is empty for \(q=2\).  Later algorithms can have different success behavior.  A residual literature risk is that the exact fiber count or the characteristic split may have appeared under different terminology in an unindexed discussion of the same measurement.

## References
1. T. Decker and P. Wocjan, *Efficient Quantum Algorithm for Hidden Quadratic and Cubic Polynomial Function Graphs*, arXiv:quant-ph/0703195, first submitted 2007-03-21.
2. T. Decker, J. Draisma, and P. Wocjan, *Efficient Quantum Algorithm for Identifying Hidden Polynomials*, arXiv:0706.1219, first submitted 2007-06-08.
3. T. Decker, G. Ivanyos, M. Santha, and P. Wocjan, *Hidden Symmetry Subgroup Problems*, arXiv:1107.2189.
4. T. Decker, P. Høyer, G. Ivanyos, and M. Santha, *Polynomial time quantum algorithms for certain bivariate hidden polynomial problems*, arXiv:1305.1543.
