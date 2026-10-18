# Elliptic Frobenius traces govern every two-sum fiber of the inverse-square curve

## Finding

Let \(q\) be any power of a prime of characteristic at least \(5\), let \(F=\mathbb F_q\), and write
\[
C=\{(t,t^{-2}):t\in F^\times\}\subseteq F^2.
\]
For \((s,y)\in F^2\), let \(r(s,y)\) be the number of **ordered** pairs \((a,b)\in(F^\times)^2\) satisfying \(a+b=s\) and \(a^{-2}+b^{-2}=y\). Set \(M_j=|\{(s,y):r(s,y)=j\}|\), let \(\chi:F\to\{0,\pm1\}\) be the quadratic character with \(\chi(0)=0\), and put \(\varepsilon=\chi(-1)\), \(\delta=\chi(-3)\), and \(\gamma=\chi(3)\).

Consider the smooth elliptic curve
\[
\mathcal A:\quad v^2=(1-4z)(1-4z^2),\qquad
 a_q=q+1-\#\mathcal A(F).
\]
Every representation multiplicity lies in \(\{0,1,2,3,4\}\); some of these levels may be absent in a particular field. The complete distribution is:
\[
\begin{aligned}
M_1&=\frac{q-1}{2}(1-\gamma),
& M_3&=\frac{q-1}{2}(1+\gamma),\\
M_2&=\frac{q-1}{4}(q+3+2\varepsilon+2\delta+a_q),
& M_4&=\frac{q-1}{8}(q-9-2\varepsilon-2\delta-2\gamma-a_q),\\
M_0&=q^2-M_1-M_2-M_3-M_4.
\end{aligned}
\]
Thus the **exact additive energy** and sumset size are
\[
\boxed{E(C)=(q-1)(3q-10-2\varepsilon-2\delta-a_q)},
\qquad
\boxed{|C+C|=\frac{q-1}{8}(3q+5+2\varepsilon+2\delta+a_q-2\gamma)}.
\]
Moreover the four-representation fibers first appear precisely at \(q=17\): \(M_4=0\) for \(q\in\{5,7,11,13\}\), while \(M_4>0\) for every eligible prime power \(q\ge17\).

## Assumptions and scope

All equations and characters are over \(F\), including nonprime finite fields. The curve \(\mathcal A\) is nonsingular in characteristic at least \(5\) because the three zeros \(1/4\), \(1/2\), and \(-1/2\) of its cubic equation are distinct. Its projective smooth completion has one rational point at infinity. The Frobenius trace is defined by the point count above. The result is for **unweighted ordered** convolutions; it does not claim a sharp extension inequality for arbitrary complex weights. Its primary subject is exact twofold convolution and the associated constant-input Fourier fourth moment.

## Proof

**1. Normalize all targets with nonzero first coordinate.** When \(s\ne0\), set \(h=ab\), \(z=h/s^2\), and \(w=s^2 y\). The monic equation for \(a,b\) has discriminant \(s^2(1-4z)\). Thus the number of ordered pairs with a prescribed \(z\in F^\times\) is
\[
\nu(z)=1+\chi(1-4z),
\]
and their target satisfies
\[
w=W(z)=\frac{1-2z}{z^2}.
\]
Hence \(r(s,y)=\sum_{z\ne0:W(z)=s^2 y}\nu(z)\). For distinct nonzero \(z,u\), an exact factorization gives
\[
W(z)=W(u)\quad\Longleftrightarrow\quad
(z-u)(2zu-z-u)=0.
\]
The off-diagonal partner, when finite, is \(T(z)=z/(2z-1)\), an involution with unique nonzero fixed point \(z=1\). Its finite-domain exclusions are \(z=0\), \(z=1/2\), and the diagonal \(z=1\).

**2. Determine the possible odd multiplicities.** The function \(\nu(z)\) takes values \(0\), \(1\), and \(2\), and it is odd only at \(z=1/4\). Its partner is \(T(1/4)=-1/2\), so the unique odd-valued normalized target is \(w=W(1/4)=8\), whose multiplicity is \(1+(1+\chi(3))=2+\gamma\). The fixed target \(w=-1\) has multiplicity \(1+\chi(-3)\) and the point \(w=0\) has multiplicity \(1+\chi(-1)\), both even. All other fibers are unions of at most two size-two quadratic fibers, so have sizes \(0,2,4\). Each nonzero \(s\) contributes exactly one fiber of size \(1\) if \(\gamma=-1\), or size \(3\) if \(\gamma=1\). At \(s=0\), the constraints force \(b=-a\) and \(y=2a^{-2}\), and all nonempty fibers have size exactly \(2\). This proves the formulas for \(M_1\) and \(M_3\), and excludes multiplicities above four.

**3. Compute the energy over one nonzero first-coordinate slice.** Write \(S_q=\sum_{z\in F}\chi((1-4z)(1-4z^2))=-a_q\). Counting equal normalized outputs gives
\[
E_s=\sum_{z\in F^\times}\nu(z)^2
+\sum_{z\in F\setminus\{0,1/2,1\}}\nu(z)\nu(Tz).
\]
The first term is \(2q-5\), using \(\sum_z\chi(1-4z)=0\) and the unique zero of \(1-4z\). In the second term, expand
\[
\nu(z)\nu(Tz)=1+\chi(1-4z)+\chi(1-4z^2)+\chi((1-4z)(1-4z^2)).
\]
The identity for \(\chi(1-4z^2)\) follows because \(\chi(1-4Tz)=\chi((1-4z^2)/(2z-1)^2)\) whenever \(2z-1\ne0\). The standard nondegenerate quadratic-character sum is \(\sum_z\chi(1-4z^2)=-\chi(-1)\). Removing the three excluded arguments and using \(\chi(9)=1\) yields the exact off-diagonal contribution
\[
q-7-2\varepsilon-2\delta+S_q.
\]
Thus
\[
E_s=3q-12-2\varepsilon-2\delta-a_q.
\]
The slice \(s=0\) contributes \(2(q-1)\) to the additive energy, because its \((q-1)/2\) nonempty target fibers all have multiplicity \(2\). Summing all \(q\) slices proves
\[
E(C)=(q-1)(3q-10-2\varepsilon-2\delta-a_q).
\]

**4. Recover the complete multiplicity distribution.** All ordered pairs give
\[
\sum_{j=0}^4jM_j=(q-1)^2,
\qquad
\sum_{j=0}^4j^2M_j=E(C).
\]
After inserting the already determined \(M_1\) and \(M_3\), subtract twice the first identity from the second to obtain \(8M_4=E(C)-2(q-1)^2+M_1-3M_3\). This gives the displayed \(M_4\). Substitution into the first identity gives \(M_2\). Finally \(\sum_{j=0}^4M_j=q^2\) gives \(M_0\), and \(|C+C|=q^2-M_0\) simplifies to the stated formula. These are exact integer identities for every eligible prime power.

**5. Sharp onset of four-representation targets.** Hasse's elliptic-curve bound \(|a_q|\le2\sqrt q\) yields
\[
\frac{8M_4}{q-1}\ge q-15-2\sqrt q>0\qquad(q\ge29).
\]
Direct exact quadratic-character calculations for the remaining eligible field sizes below \(29\), namely \(5,7,11,13,17,19,23,25\), give respectively
\[
M_4=0,0,0,0,16,36,66,48.
\]
For \(q=25\) the finite-field value also follows from the elementary Frobenius recurrence \(a_{25}=a_5^2-10=-6\). Therefore \(q=17\) is the sharp onset. The same recurrence \(a_{p^m}=a_p a_{p^{m-1}}-p a_{p^{m-2}}\) for \(m\ge2\), initialized with \(a_{p^0}=2\), recovers the spectrum throughout any extension tower from one elliptic point count.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It enumerates all ordered pairs independently of the proof, then checks the exact energy and **each** of the five target-multiplicity counts against the formulas. Prime-field tests cover \(q=5,7,11,13,17,19,23,29,31,37,41\). Tests over genuine nonsplit quadratic extensions cover \(q=25,49,121,169\), with field multiplication and inversion implemented directly. All cases print `VERIFICATION_OK`, and the exact observed output is included in `verification_output.txt`. The computation checks finite cases only; the argument in the Proof establishes the all-field theorem.

For any fixed nontrivial additive character \(\psi\), character orthogonality additionally gives the fourth-moment interpretation
\[
\frac1{q^2}\sum_{(\xi,\eta)\in F^2}
\left|\sum_{t\in F^\times}\psi(\xi t+\eta t^{-2})\right|^4=E(C).
\]

## Relationship to prior work

The 2024 finite-field sharp-extension work of González-Riquelme and Oliveira e Silva treats paraboloids, quadratic cones, and hyperbolic paraboloids and motivates the fourth-moment/convolution question; its listed surfaces do not include the inverse-square curve. The related finite-field multiplicative hyperbola \((t,t^{-1})\) concerns a degree-two affine curve, not \(t^2y=1\), and its known sharp fourth-moment result does not supply these elliptic-trace fibers. A published fifth-power polynomial-graph two-sum classification concerns \((t,t^5)\); no affine change of variables preserves sums while identifying that polynomial graph with the inverse-square cubic. The present result is a distinct **complete representation spectrum**, with a genuinely variable elliptic Frobenius trace and the sharp fourfold-fiber threshold.

## Limitations

The theorem makes no assertion about all complex-weight extremizers or the sharp operator norm. The Frobenius trace \(a_q\) is an exact point-count invariant, not generally an elementary congruence-class constant; an explicit field-specific numerical value requires counting points or applying a point-count algorithm. The originality assessment is best-knowledge rather than an independence guarantee; existing special-function or elliptic-sum literature may contain an equivalent formula. No independent audit has been carried out.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (first publicly available 2024-05-26), https://arxiv.org/pdf/2405.16647.
2. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, Discrete Analysis (2018), arXiv:1801.03176, https://arxiv.org/abs/1801.03176 (broader restriction context, not this curve).
3. Hasse's theorem for elliptic curves over finite fields: \(|a_q|\le2\sqrt q\) (standard elliptic-curve point-count bound).
