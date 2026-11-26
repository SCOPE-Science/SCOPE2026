# Independent mathematical audit

## correctness

PASS

The coefficient recurrence gives the exact sum S_k=(2k+1)a_k. After summation by parts, bounded variation of sqrt(t)*exp(wt) on [0,1] and the summed O((k+1)^(-1/2)) coefficient errors give P_n(exp(w/n))/sqrt(n)=H(w)+O_R(1/n) uniformly on every fixed disk |w|<=R. For Re w<=0 and Im w>0, integration by parts of the sine integral against (1-cos(yt))/y gives a nonnegative endpoint term and a strictly positive integral, because t^(-1/2)*exp(Re(w)t) is strictly decreasing; the term at zero vanishes like t^(3/2). Conjugation and positivity on the real axis finish exclusion. Zero-free exponential type would force H to be an exponential of a linear polynomial, incompatible with H(-R) comparable to R^(-1/2). The differential identity H+2wH'=2exp(w)/sqrt(pi) gives simplicity. The oscillatory term in bounded real-part strips is the nonzero leading Fresnel term exp(i sign(y) pi/4)/sqrt(|y|): subtracting the weight at zero gives an absolutely integrable derivative for the remainder and an O(1/|y|) bound. Thus a zero exists and c_* is a strictly positive attained minimum. Global angular exclusion is decisive: with d_k=a_(k-1)-a_k one has (1-z)P_n(z)=Q_n(z)-a_n*z^(n+1), where Q_n is the truncation of sqrt(1-z). Its unit-circle error is bounded by a_n. At z=rho*u in the candidate collar, rho^k-1<=k(rho-1)rho^(k-1) and sum(k*d_k)=S_(n-1)/2=O(sqrt(n)), so Q_n(rho*u)-Q_n(u)=O_C(n^(-1/2)). At a zero this forces sqrt(|1-u|)=O_C(n^(-1/2)) and a bounded scaled logarithm. Strict coefficient ratios exclude all |z|<=1. Rouché on a circle of radius M/n at a simple minimizing H zero gives a candidate, and on the resulting fixed compact set of possible scaled nearest roots the pointwise bound |H|=O(1/n) forces distance O(1/n) to a simple H zero. Exponentiating yields the claimed O(n^(-2)) radial remainder on both sides. The uploaded checker was inspected, not executed; its Newton solves follow one local branch, and the polynomial coefficient recurrence also uses a Python floating ratio before multiplying the high-precision values. Neither that computation nor a certified numerical value of c_* is needed.

## originality

PASS

The supported contribution is the global minimum-modulus asymptotic and its remainder for the precise central-binomial section sequence, not local scaling or an error-function zero in isolation. The same problem appears in Technau with a logarithmic gap, and the available nearby section and incomplete-beta results do not give the uniform complex collar localization needed for the global minimum. The historical priority check is bounded; unresolved same-family older sources are named below without assigning them a noncoverage verdict.

## value

PASS

It resolves Technau’s explicit nearest-zero asymptotic question for a classical family by removing the full logarithmic uncertainty, gives a strictly positive well-defined sharp constant, and improves the radial remainder to second order. The proof isolates why local scaling captures the true global minimum, a useful distinction in section-zero problems. It is not a claim to solve the larger Shapiro coefficient problem or to numerically certify the identity of the extremizing zero.

The dated certificate retains the supplied scientific assessment, sources and limitations.
