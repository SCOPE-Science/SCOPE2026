# Independent mathematical audit

## correctness

PASS

With conserved opposite currents J and −J, the two stationary densities are uniquely fixed up to J by the wall values J/κ, and reflection exchanges them. For example ρ_+(x)=J/v+(J/κ−J/v)e^(p(x/L−1)), nonnegative for J>0 as a convex combination of the two endpoint coefficients. Normalization fixes J and yields c=p/(p+β−1+e^−p); the denominator is positive. The centered cosh density has second moment 1/4+2/p²−coth(p/2)/p. Its strict positive excess over 1/12 follows by strict positive covariance of y² with the cosh weight under the uniform law. Thus the sign is that of β−1+e^−p. The objective tends to 1/12 at p→0 and p→∞; when 0<β<1 the positive gain after H guarantees an interior global optimum. For δ→0, the test p=H+log H gives gain ∼δ/(6H), while p≥(1+ε)H has gain bounded by δ/[6((1+ε)H−δ)]; hence every optimum has p/H→1. Writing u=e^−p, log differentiation of the gain gives u/(δ−u)=(1−u)/(p−δ+u)−B′/B, with B′/B=6/p²+O(p^−3). Converting the resulting 1/p−6/p² to u/δ contributes one more unit, giving 1/p−7/p²+O(p^−3). Taking logarithms and expanding about H gives the stated optimizer; the gain at that point is δ/(6p)(1−7/p+O(p^−2)), yielding the stated depth. No uniqueness of the optimizer is used.

## originality

PASS

Pass is limited to the fixed-β singular optimization near β=1: location of every global minimizer through the term with constant 7, and depth through the displayed next order. The stationary solution and variance are already in Roberts–Pruessner and credited as inputs. The sign threshold is already encoded by their density-shape crossover and variance, and is not separately credited as novel. The inspected passages and nearest indexed results do not give the singular optimum law.

## value

PASS

Even with an exact stationary variance, the weak-confinement design problem near threshold has a diverging optimizer and a shrinking depth. The log-log scale separates the optimum from the sign-change point, and the paired location and depth coefficients quantify the singular balance under a natural fixed-rates length variation. This adds more than rewriting the known variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
