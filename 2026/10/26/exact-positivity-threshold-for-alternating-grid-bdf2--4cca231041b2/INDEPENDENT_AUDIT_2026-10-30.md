# Independent mathematical audit

## correctness

PASS

The variable-step BDF2 recurrence is (1+2r_n+(1+r_n)z_n)y_n=(1+r_n)^2 y_(n-1)-r_n^2 y_(n-2). Ratios q_n=y_n/y_(n-1) obey alternating Möbius maps. The long-to-long map F(q)=c_H-d_H/(c_L-d_L/q) has positive fixed points controlled by p(q)=c_L q^2-(c_H c_L-d_H+d_L)q+c_H d_L, whose discriminant factors by (r-1)^2 z^2-4(r+1)z+4. The first real-root-loss boundary is z_-=2/(sqrt(r)+1)^2. Below and at it B>2d_L, the largest fixed point q_+ lies in q>d_L/c_L and exact startup algebra gives q1>=q_+, so monotone iteration preserves every long/short ratio strictly positive, including repeated-root equality. Above it p(q)>0 throughout positive domain (either discriminant negative or B<0 after the second root), forcing long-step ratios to decrease and ultimately cross the short-step positivity boundary; hence some iterate is nonpositive. Independent SymPy discriminant check and rational time-stepping r=1,4,9,16 both sides passed; finite tests alone are not infinite necessity proof.

## originality

PASS

The r=1 constant-step threshold 1/2 is prior, including published Resultary delayed-sign-loss treatment. Earlier full primary studies of variable-step BDF2 establish stability/error bounds or Allen--Cahn maximum-principle sufficient conditions, not the all-index necessary-and-sufficient scalar alternating-grid threshold for each r>=1. The method of Floquet/two-step recurrences is standard, but the exact sharp boundary and its repeated-root inclusion supply a new precise numerical-analysis fact.

## value

PASS

Positivity preservation is an independent, physically significant criterion for numerical decay schemes that conventional stability bounds do not determine. The sharp long/short tradeoff and exact equality case prevent unsupported safe-step claims and show how larger isolated long steps become possible; the parameter family is motivated rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
