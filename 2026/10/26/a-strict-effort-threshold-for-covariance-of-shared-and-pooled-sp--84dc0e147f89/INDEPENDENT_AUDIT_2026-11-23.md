# Independent mathematical audit

## correctness

PASS

For any pair of species indicators, write U_j as one minus the two-survey absence indicator. The intersection of S_i=1 with U_j=0 has probability 0 for i=j and (a-b)^2 for i≠j, with a=t^n and b=((m-2)/m)^n. Thus the covariance sum is m^2 a^2(1-a)^2-m(m-1)(a-b)^2 and factors exactly as claimed. Conditioning on the first survey gives expectations (1-a)|A| and m(1-a)+a|A|; the conditional covariance is |A|(m-|A|)(b-a^2), confirming the competing signs. R_x increases strictly since z/(exp(xz)-1) decreases strictly in z>0, with a separate s=0 proof at m=2. It starts below sqrt(t) at x=1 (R_1=t) and tends to one. At integer effort R_n is rational, but sqrt((m-1)/m) cannot be rational: the coprime consecutive positive numerator and denominator would both have to be squares. For n=floor(cm), log s-log t=-1/m^2+O(m^-3), so s^n-t^n=-c exp(-c)/m+O_c(m^-2), and division by 1-s^n gives the stated expansion for R_n. Comparing the first-order coefficient to that of sqrt(t), and bracketing above and below the unique positive zero of exp(c)-1-2c, proves the sharp limit without claiming finite equality. A fresh exact occupied-mask recurrence reproduced all 25 moment comparisons for 2<=m<=6, 1<=n<=5, including covariances -1/4 and 1/64 at m=2. First-positive efforts (2,4,5,6,8,13) at the displayed community sizes and the signs through n_*+10 for 2<=m<=50 agreed. Exact Taylor bounds bracketed alpha in (1.2564312086,1.2564312087). Replay details: replays/1.md. Packaged source and output were inspected rather than executed. The documented Python 3.8 minimum is too low for int.bit_count (introduced in 3.10); this is a reproducibility note, not a mathematical defect. The finite checks do not prove the unrestricted threshold, irrationality or limit.

## originality

PASS

Best-of-knowledge pass for the strict common-effort switch, no integer ties and its limiting threshold. The incidence observables and empty-cell indicator calculus are established tools, not independent novelty claims. Primary-text comparisons support this limited assessment; unavailable lookups do not support a claim of absence.

## value

PASS

This is a natural paired-survey statistic: the covariance is the cross-term between the numerator and denominator of incidence similarity, not a marginal variance. Changing effort alone in the homogeneous baseline reverses it. A single switch with a sharp scaling constant is a structural conclusion beyond the routine indicator computation and gives a benchmark for more realistic sampling models. It does not estimate a field confidence interval or determine the behavior of the ratio itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
