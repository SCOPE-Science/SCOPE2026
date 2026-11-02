# Second-order optimality gaps for the two sharp modified-Bessel product bounds

## Finding
For real orders \(\nu\geq 1\) and positive \(x\), define the product, its normalized inverse square, and its logarithmic-derivative companion by
\[
P_\nu(x)=I_\nu(x)K_\nu(x),\quad
h_\nu(x)=\frac1{4P_\nu(x)^2}-x^2-\nu^2,\quad
H_\nu(x)=-\frac{xP_\nu(x)}{P_\nu'(x)}-x^2-\nu^2.
\]
The derivative of \(P_\nu\) is strictly negative in this range, so both expressions are defined. Put \(c_\nu=\max_{x>0}h_\nu(x)\) and \(d_\nu=\max_{x>0}H_\nu(x)\). These are the optimal order-dependent additive constants in the two respective one-sided modified-Bessel inequalities.

**Theorem.** As \(\nu\to+\infty\) through real values,
\[
c_\nu=\frac15-\frac{54}{625\nu^2}+O(\nu^{-4}),\qquad
 d_\nu=\frac7{20}-\frac{108}{625\nu^2}+O(\nu^{-4}).
\]
There exists a finite \(\nu_0\) such that for every \(\nu>\nu_0\) each maximum is attained at a unique positive argument, respectively \(x_{h,\nu}\) and \(x_{H,\nu}\). The maximizing rays satisfy
\[
\frac{x_{h,\nu}}\nu=\sqrt{\frac23}+\frac{17\sqrt6}{150\nu^2}+O(\nu^{-4}),\qquad
\frac{x_{H,\nu}}\nu=\sqrt{\frac32}+\frac{27\sqrt6}{80\nu^2}+O(\nu^{-4}).
\]
The constants \(54/625\) and \(108/625\) therefore give the exact first nonzero deficits of the **optimal fixed-order** shifts, not merely values along prescribed rays.

## Assumptions and scope
The order \(\nu\) is any sufficiently large positive real, not necessarily integral. The argument is an arbitrary positive real. Modified Bessel functions use their standard positive-real normalizations. The maximizing arguments are unique only as asserted for sufficiently large order; no all-order uniqueness claim is made. Big-O constants are absolute as \(\nu\to+\infty\), and maxima here are over the entire unbounded positive half-line.

## Proof
**1. Endpoint behavior and existence.** The established sharp inequalities and endpoint limits of Segura--Suzuki (Sections 2--5 of the cited paper) give, for \(\nu\ge1\),
\[
-\tfrac14<h_\nu(x)<\tfrac15,\qquad -1<H_\nu(x)<\tfrac7{20};
\]
moreover \(h_\nu(0^+)=0\), \(h_\nu(+\infty)=-1/4\), \(H_\nu(0^+)=-1\), and \(H_\nu(+\infty)=-1/4\). The fixed-ray leading Debye expansions, proved below, give positive values approaching \(1/5\) and \(7/20\), respectively. Consequently, the two global maxima are attained at interior points for all sufficiently large \(\nu\), and \(c_\nu\to1/5\), \(d_\nu\to7/20\).

**2. A global localization lemma.** Set \(q_\nu(x)=x^2+\nu^2+h_\nu(x)\) and \(Q_\nu(x)=x^2+\nu^2+H_\nu(x)\). Segura--Suzuki's exact differential identities (their equations (3.2) and (4.2)) are
\[
4x^2q_\nu h_\nu''+(4xq_\nu-5x^2q_\nu'-10x^3)h_\nu'-16q_\nu^2h_\nu
 =20x^4-16x^2q_\nu,
\]
\[
x^2Q_\nu H_\nu''+(5xQ_\nu-2x^2Q_\nu'-7x^3)H_\nu'-4Q_\nu^2H_\nu
 =15x^4-18x^2Q_\nu+4Q_\nu^2.
\]
At a global maximum the first derivative vanishes and the second derivative is nonpositive. Because the coefficients of the second derivatives are positive, rearrangement gives the exact restrictions
\[
h_\nu(x)\le\frac15-\frac54\left(\frac{x^2}{q_\nu(x)}-\frac25\right)^2,
\]
\[
H_\nu(x)\le\frac7{20}-\frac{15}{4}\left(\frac{x^2}{Q_\nu(x)}-\frac35\right)^2,
\]
where each inequality is asserted **at a maximizer of its left-hand side**, not pointwise for arbitrary \(x\). Since the two maximal values tend to their respective universal upper bounds, the squared terms must tend to zero at **every** global maximizer. Since the corresponding \(h_\nu\) and \(H_\nu\) are uniformly bounded, \(q_\nu(x)=x^2+\nu^2+O(1)\) and \(Q_\nu(x)=x^2+\nu^2+O(1)\). Thus every maximizing sequence obeys
\[
\frac{x}{\nu}\longrightarrow\sqrt{\frac23}\quad\text{for }h_\nu,
\qquad
\frac{x}{\nu}\longrightarrow\sqrt{\frac32}\quad\text{for }H_\nu.
\]
This localization requires no unjustified extrapolation of fixed-ray asymptotics to an unbounded interval.

**3. Two full Debye coefficients.** Put \(z=x/\nu>0\) and \(p=(1+z^2)^{-1/2}\). On every compact subinterval of \(z>0\), the classical differentiated Debye expansions (DLMF Section 10.41(ii), equations 10.41.3--10.41.9) yield, with the needed derivatives,
\[
P_\nu(\nu z)=\frac{p}{2\nu}\left(1+\frac{A(p)}{\nu^2}+\frac{B(p)}{\nu^4}+O(\nu^{-6})\right),
\]
where the odd inverse-order terms cancel between the expansions for \(I_\nu\) and \(K_\nu\), and
\[
A(p)=\frac{p^2(p^2-1)(5p^2-1)}8,
\quad
B(p)=\frac{p^4(p^2-1)(1155p^6-1617p^4+553p^2-27)}{128}.
\]
These polynomials follow by multiplying the Debye series and using the DLMF recurrence for their coefficient polynomials. Algebraic inversion and logarithmic differentiation give the following expansions, valid locally in \(C^2\):
\[
h_\nu(\nu z)=h_0(z)+\nu^{-2}h_2(z)+O(\nu^{-4}),
\quad
H_\nu(\nu z)=H_0(z)+\nu^{-2}H_2(z)+O(\nu^{-4}),
\]
\[
h_0(z)=\frac{z^2(4-z^2)}{4(1+z^2)^2},
\quad
h_2(z)=-\frac{z^2(3z^6-56z^4+68z^2-8)}{8(1+z^2)^5},
\]
\[
H_0(z)=-\frac{z^4-10z^2+4}{4(1+z^2)^2},
\quad
H_2(z)=-\frac{3z^2(2z^6-59z^4+136z^2-48)}{8(1+z^2)^5}.
\]
The explicit correction polynomials can also be reconstructed independently by substituting power-series ansätze into the exact equations (3.1) and (4.7) of Segura--Suzuki.

**4. Optimization and exact constants.** The rational leading profiles have unique strict global maxima
\[
h_0(z_h)=\frac15,\quad z_h=\sqrt{\frac23},\quad h_0''(z_h)=-\frac{108}{125};
\]
\[
H_0(z_H)=\frac7{20},\quad z_H=\sqrt{\frac32},\quad H_0''(z_H)=-\frac{144}{125}.
\]
By Step 2, every global maximizer of either family lies eventually in a fixed small compact neighborhood of its corresponding leading maximum. By \(C^2\) convergence in Step 3, the exact profile is strictly concave throughout that neighborhood for sufficiently large \(\nu\). Hence there is exactly one global maximizer in each family. Expanding the vanishing derivative at that point gives
\[
\frac{x_{h,\nu}}\nu=z_h-\frac{h_2'(z_h)}{h_0''(z_h)}\nu^{-2}+O(\nu^{-4}),
\quad
\frac{x_{H,\nu}}\nu=z_H-\frac{H_2'(z_H)}{H_0''(z_H)}\nu^{-2}+O(\nu^{-4}).
\]
Exact substitution gives
\[
h_2(z_h)=-\frac{54}{625},\quad
-\frac{h_2'(z_h)}{h_0''(z_h)}=\frac{17\sqrt6}{150};
\]
\[
H_2(z_H)=-\frac{108}{625},\quad
-\frac{H_2'(z_H)}{H_0''(z_H)}=\frac{27\sqrt6}{80}.
\]
Evaluating the profiles at the shifted maximizers changes their values only at order \(\nu^{-4}\) beyond their stated \(\nu^{-2}\) corrections, proving both optimality-gap expansions. This completes the proof.

## Verification
`CHECK.py` independently generates the first four Debye coefficient polynomials from the DLMF recurrence, checks the product's order-two and order-four coefficients, derives the two correction profiles directly from the product, evaluates exact algebraic maxima and shifts, and verifies the local-max localization inequalities as polynomial identities. It also performs supplementary numerical maximizations for several fixed large orders using scaled modified Bessel functions. Run `python CHECK.py` with the versions specified in `requirements.txt`; the expected final line is `CHECK_OK 33`. This script does not replace the analytic compact-asymptotic/localization argument.

## Relationship to prior work
Segura and Suzuki, arXiv:2610.07933 (first posted 2026-10-06), prove the universal sharp bounds \(1/5\) and \(7/20\), derive the leading fixed-ray profiles, and tabulate numerical maximizers. Their Section 5 identifies the limiting maximizing rays but does not compute the rigorous optimal fixed-order inverse-square deficits, corrected optimizer positions, or eventual uniqueness. The present calculation retains their definitions and differential identities, and adds a global-extremum localization step and next Debye coefficients.

Segura, arXiv:2608.03633 (first posted 2026-08-04), already derives a fourth-order Debye term on the **single critical product ray**. That term permits recovery of the product's pointwise correction at the limiting ray, but it neither proves that this pointwise value gives the next term of the **global supremum** nor gives the logarithmic-derivative family's optimal correction or the two optimizer shifts. Segura's 2021 ratio/product monotonicity results similarly do not determine these extremal asymptotics. The DLMF coefficient formulas themselves are classical; novelty is not claimed for the Debye method or its coefficient recurrence.

## Limitations
This theorem is asymptotic as real \(\nu\to+\infty\). It neither gives exact finite-order sharp constants nor an explicit numerical value of \(\nu_0\). The \(O(\nu^{-4})\) remainders are not presented with computable absolute bounds. The proof relies on the standard all-orders differentiated Debye expansion on compact positive rays and on established sharp Bessel inequalities and exact differential identities. It does not claim independence from those theorems. Earlier unindexed treatment of the same *optimized* inverse-square defects remains a literature risk.

## References
1. J. Segura and S. Suzuki, *Sharp two-sided bounds for the product of modified Bessel functions and for its logarithmic derivative*, arXiv:2610.07933v1, 2026-10-06. https://arxiv.org/html/2610.07933v1
2. J. Segura, *Optimized bounds for the product and the ratios of modified Bessel functions*, arXiv:2608.03633, 2026-08-04. https://arxiv.org/abs/2608.03633
3. J. Segura, *Monotonicity properties for ratios and products of modified Bessel functions and sharp trigonometric bounds*, Results in Mathematics 76 (2021), article 221; arXiv:2105.02524. https://link.springer.com/article/10.1007/s00025-021-01531-1
4. NIST Digital Library of Mathematical Functions, Section 10.41(ii), especially 10.41.3--10.41.9 (uniform modified-Bessel expansions and coefficient recurrence). https://dlmf.nist.gov/10.41
