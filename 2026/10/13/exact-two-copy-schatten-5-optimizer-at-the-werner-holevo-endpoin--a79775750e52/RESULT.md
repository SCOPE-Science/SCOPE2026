# Exact two-copy Schatten-\(5\) optimizer at the Werner--Holevo endpoint
## Finding
For the qutrit Werner--Holevo channel
\[
\Phi_3(X)=\frac12\left(\operatorname{Tr}(X)I-X^{\mathsf T}\right),
\]
the maximal output Schatten-\(5\) norm of two copies is
\[
\nu_5(\Phi_3\otimes\Phi_3)^5=\frac{43}{10368},
\qquad
\nu_5(\Phi_3\otimes\Phi_3)=\left(\frac{43}{10368}\right)^{1/5}.
\]
Among pure bipartite inputs, equality holds exactly for Schmidt probabilities \((1/3,1/3,1/3)\), hence exactly for maximally entangled qutrit inputs up to local unitaries. Since a single use has output spectrum \((1/2,1/2,0)\) on every pure input,
\[
\nu_5(\Phi_3)=2^{-4/5},
\qquad
\frac{\nu_5(\Phi_3\otimes\Phi_3)}{\nu_5(\Phi_3)^2}
=\left(\frac{86}{81}\right)^{1/5}>1.
\]
Thus \(p=5\), the first integer above the classical Werner--Holevo threshold near \(4.7823\), admits an exact global optimizer and an exact violation factor.

## Assumptions and scope
The channel is the lower endpoint \(t=-1/(d-1)\), with \(d=3\), of the transpose-depolarizing family
\[
\Phi_t(X)=tX^{\mathsf T}+(1-t)\operatorname{Tr}(X)I/d.
\]
The quantity \(\nu_5\) is the maximal output Schatten norm, maximized over all density operators. Convexity reduces the optimization to pure inputs. Covariance reduces a pure bipartite input to Schmidt form with probabilities \(\lambda_1,\lambda_2,\lambda_3\ge0\) and \(\lambda_1+\lambda_2+\lambda_3=1\).

The claim is only about two identical qutrit Werner--Holevo channels and exponent \(5\). It does not locate the exact real transition exponent, prove an optimizer theorem for arbitrary real \(p>4.7823\), or address general transpose-depolarizing parameters.

## Proof
Write
\[
e_2=\lambda_1\lambda_2+\lambda_2\lambda_3+\lambda_3\lambda_1,
\qquad
e_3=\lambda_1\lambda_2\lambda_3.
\]
At the Werner--Holevo endpoint, the two-copy output has six off-diagonal-sector eigenvalues \(\lambda_i/4\), each \(\lambda_i/4\) occurring twice. On the span of \(|11\rangle,|22\rangle,|33\rangle\), four times the remaining block is
\[
B=\operatorname{diag}(1-2\lambda_1,1-2\lambda_2,1-2\lambda_3)+vv^{\mathsf T},
\qquad
v=(\sqrt{\lambda_1},\sqrt{\lambda_2},\sqrt{\lambda_3})^{\mathsf T}.
\]
If \(\gamma_1,\gamma_2,\gamma_3\) are the eigenvalues of \(B\), the matrix-determinant lemma and \(\lambda_1+\lambda_2+\lambda_3=1\) give
\[
\prod_{j=1}^3(x-\gamma_j)=x^3-2x^2+x-4e_3.
\]
Hence the remaining output eigenvalues are \(\gamma_j/4\).

Newton identities for \(\lambda_1,\lambda_2,\lambda_3\), whose elementary symmetric functions are \(1,e_2,e_3\), give
\[
\sum_i\lambda_i^5=5e_2^2-5e_2e_3-5e_2+5e_3+1.
\]
Newton identities for the cubic above give
\[
\sum_j\gamma_j^5=60e_3+2.
\]
Therefore
\[
4^5\operatorname{Tr}\!\left[(\Phi_3\otimes\Phi_3)(|\psi\rangle\langle\psi|)^5\right]
=10e_2^2-10e_2e_3-10e_2+70e_3+4.
\]
Because \(0\le e_2\le1/3\), the coefficient \(70-10e_2\) of \(e_3\) is positive. Maclaurin's inequality gives
\[
e_3\le\left(\frac{e_2}3\right)^{3/2}.
\]
Set \(u=\sqrt{e_2/3}\), so \(0\le u\le1/3\). The numerator is bounded by
\[
f(u)=4-30u^2+70u^3+90u^4-30u^5.
\]
The exact difference from the value at \(u=1/3\) factors as
\[
\frac{344}{81}-f(u)
=\frac{10}{81}(3u-1)
\left(81u^4-216u^3-261u^2-6u-2\right).
\]
For \(0\le u\le1/3\), one has \(81u^4\le27u^3\), so the quartic factor is strictly negative, while \(3u-1\le0\). Thus \(f(u)\le344/81\), with equality only at \(u=1/3\). Equality in the preceding Maclaurin bound at this point forces \(\lambda_1=\lambda_2=\lambda_3=1/3\). Dividing by \(4^5\) gives
\[
\max\operatorname{Tr}(\text{output}^5)=\frac{344/81}{1024}=\frac{43}{10368}.
\]
Finally, \(\nu_5(\Phi_3)^5=1/16\), so the fifth power of the multiplicativity ratio is
\[
\frac{43/10368}{1/256}=\frac{86}{81}.
\]

## Verification
The analytic proof uses only the channel eigenvalue reduction, Newton identities, Maclaurin's inequality, and the displayed polynomial factorization. The bundled `verify_wh_p5.py` checks the two Newton recurrences, the factorization, the exact uniform value \(43/10368\), and the exact fifth-power violation ratio \(86/81\) using rational arithmetic. It also checks the upper-bound polynomial on a deterministic rational grid as a supplementary sanity test.

## Relationship to prior work
Datta, Holevo, and Suhov treat the transpose-depolarizing family and identify its lower endpoint as the Werner--Holevo channel. Their full text derives the Schmidt-simplex output matrix and its eigenvalue equations, then proves additivity of minimum output entropy across the full parameter range; the associated maximal-output \(p\)-norm results are confined to the low-\(p\) regime.

Werner and Holevo introduced the endpoint counterexample and found the real threshold numerically near \(4.7823\). Their paper explicitly states that at \(p=5\) the global maximum moves from product-state corners to the maximally entangled center, but says this is seen by plotting over the Schmidt parameters. The present result proves that \(p=5\) statement globally, gives uniqueness at the Schmidt-spectrum level, and evaluates the exact maximum and violation factor.

Datta later proved multiplicativity for Werner--Holevo channels for \(1\le p\le2\), using the same Schmidt-simplex framework. That theorem does not imply the \(p=5\) maximum and in fact lies on the opposite side of the multiplicativity transition.

## Limitations
No claim is made about the exact noninteger transition exponent, the full optimizer phase diagram in \(p\), more than two channel copies, dimensions other than three, or nonendpoint transpose-depolarizing parameters. Exact-string, alias, implication, and database searches found no publication giving the displayed \(43/10368\) optimum or \((86/81)^{1/5}\) violation factor; an equivalent derivation could nevertheless exist in poorly indexed notes or theses. The original \(p=5\) optimizer was already asserted from numerical plots, so originality here is specifically the exact analytic global proof, uniqueness statement, and exact value.

## References
1. N. Datta, A. S. Holevo, and Y. Suhov, *Additivity for transpose depolarizing channels*, arXiv:quant-ph/0412034; DOI:10.1142/S0219749906001633.
2. R. F. Werner and A. S. Holevo, *Counterexample to an additivity conjecture for output purity of quantum channels*, arXiv:quant-ph/0203003; DOI:10.1063/1.1498491.
3. N. Datta, *Multiplicativity of Maximal p-Norms in Werner-Holevo channels for 1 <= p <= 2*, arXiv:quant-ph/0410063.
4. A. S. Holevo, *Multiplicativity of p-norms of completely positive maps and the additivity problem in quantum information theory*, Russian Mathematical Surveys 61 (2006), 301--339; DOI:10.1070/RM2006v061n02ABEH004313.
