# Three sign changes in singleton–doubleton covariance for three unequal boxes

## Finding

Independently allocate each of \(n\) balls to one of three boxes with probabilities \((1,15,16)/32\). Let \(X_r\) count boxes containing exactly \(r\) balls. As \(n\) varies, \(\operatorname{Cov}(X_1,X_2)\) has at least three strict sign reversals: it has signs \(+,-,+,-\) at \(n=3,4,9,10\), respectively. In particular, the nonempty positive phase of the uniform model need not remain a single interval under unequal probabilities. Three boxes suffice and are minimal for three sign reversals for this pair of loads over \(n\ge3\).

## Assumptions and scope

The box probabilities are fixed as \(n\) varies, and allocations are independent. The covariance is unconditioned beyond the fixed sample size and fixed probabilities. A strict reversal means a change between successive nonzero signs, ignoring zero terms. The four checkpoints give a lower bound, not a characterization of all sample sizes.

## Proof

Write \(d=(1,15,16)\). For a triple \(c=(c_1,c_2,c_3)\) of nonnegative occupancies summing to \(n\), put
\[
w(c)=\frac{n!}{c_1!c_2!c_3!}\prod_{i=1}^{3} d_i^{c_i},\qquad
x_r(c)=\#\{i:c_i=r\}.
\]
The probability of \(c\) is \(w(c)/32^n\). Define the integers \(A_r=\sum_c w(c)x_r(c)\) for \(r=1,2\), and \(B=\sum_c w(c)x_1(c)x_2(c)\). The covariance is exactly \((32^n B-A_1A_2)/32^{2n}\). Evaluating the sums gives:

| \(n\) | Exact covariance |
|---:|---:|
| 3 | \(427917/4194304\) |
| 4 | \(-10632785853/34359738368\) |
| 9 | \(464148085603947606981/1208925819614629174706176\) |
| 10 | \(-189451469679866467748560575/158456325028528675187087900672\) |

Thus each successive pair of checkpoints contains at least one strict sign reversal. With two boxes and strictly positive probabilities, at \(n=3\) the two counts are both the same indicator of the occupancy split \(1+2\); its variance is positive. For every \(n>3\) there cannot be both a singleton and a doubleton at once, but each event has positive probability. The covariance is then \(-\mathbb E X_1\,\mathbb E X_2<0\). One box, or a degenerate two-box distribution with one occupied support point, has deterministic counts. This proves the stated minimality.

## Verification

Run `python3 verify.py`. The standalone standard-library program enumerates ordered allocations of up to ten balls, accumulates exact integer weights, and checks the four rational covariances. The two-box argument is analytic.

## Relationship to prior work and limitations

The one-positive-interval result under uniform probabilities follows from the decreasing adjacent quotient of the normalized cross-moment (see *A single covariance window for distinct occupancy frequencies*, Resultary record `46bdb4d9ec77`). The result above is an explicit obstruction to extending that conclusion to fixed unequal probabilities; it does not claim novelty for the uniform theorem or the multinomial moment calculation. The related *A minimal three-species counterexample to one-switch richness–frequency covariance*, record `d3caf6abcfaa`, varies the frequency index and pairs the frequency count with richness at a fixed sample size. Here the pair of frequencies is fixed and the sample size varies. No all-parameter classification for unequal box probabilities or upper bound on the number of reversals is asserted.
