# Independent mathematical audit

## correctness

PASS

A positive scale change reduces the rate to one. Differentiating the given copula and changing variables to (X,S) cancels the common factor e^(-s) on the slice; H=1+θ(1−2u)(1−2v)>0 on 0<x<s even for |θ|=1. Set A=1−2u. Direct differentiation gives H_x=2θ(u−v), H_s=2θvA, H_xs=2θv, hence H² times the mixed log derivative equals 2θv(1+θA²). Integrating in s yields the positive/zero/negative sign for the common-support likelihood ratio because normalizers do not depend on x. Nested support extends the increasing ratio to the new right tail for θ≥0; even the constant common-support ratio at θ=0 implies strict CDF order by the positive added tail, since the conditional larger-sum law restricted to the old support is already weakly stochastically larger there. For θ=−r, integration of the explicit mixture of H_0 and H_−1 gives N=(1−r)t+2r(c+zd) and Z=(1−r)s+4r[1−(1+s)z]. Expanding the derivative numerator in (1−r)², r(1−r), and r² gives exactly the three negative terms in RESULT.md. With d<0, (1+s)z decreases and c+(1+t)e^(−t)d is positive by the stated positive Taylor tail. The last brace sc+(1−z)d starts positive at s=t and its derivative is bounded below by 2[1−(1+t)e^(−t)]>0. With d≥0 it is immediate. At r=0 or 1 the remaining term is strictly negative. Thus the CDF strictly decreases at each t in the common interior; between supports the strict difference follows from positive density. The continuous strictly increasing CDFs make each interior quantile strictly increase with s. Exchangeable symmetry gives Q_s(1−a)=s−Q_s(a); using one U and the two probabilities U and 1−U realizes both conditionals with strictly increasing coordinates.

## originality

PASS

The supported distinct result is strict conditional vector usual order throughout the negative FGM regime for equal-rate exponentials, despite strict failure of increasing conditional LR order there. The nonnegative-parameter sufficient theory, Efron-type questions, and FGM sum-ageing literature are acknowledged, not presented as new. Direct statements and their assumptions in the closest available sources and distinct catalogue records do not cover the negative-parameter physical-sum result.

## value

PASS

The dependent version of conditional-sum monotonicity is an established risk-allocation and stochastic-order problem. The entire negative dependence range gives a motivated, exact separation: each sum increase permits strict simultaneous coordinate growth, while the increasing conditional likelihood-ratio order fails for every distinct pair of sums. This establishes more than a finite case or a restatement of a sufficient positive-dependence criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
