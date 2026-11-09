# Independent mathematical audit

## correctness

PASS

On the 2pi circle and intrinsic angular distance with cutoff pi/2, normalized Fourier coefficients are A_|n|/pi, A_n=int_0^{pi/2}(1-sin^alpha t) cos(nt) dt. Differentiating sin^(alpha+1)(t)cos((n-1)t) yields (alpha+n)I_n+(alpha-n+2)I_(n-2)=2cos((n-1)pi/2). Even I_(2k) are negative for 0<alpha<2, making A_(2k)>0, while for alpha>2 A4=-alpha(alpha-2) I0/[(alpha+2)(alpha+4)]<0. Odd A1=alpha/(alpha+1), A3=alpha(5-alpha)/[3(alpha+1)(alpha+3)], and A5=alpha(alpha^2-16alpha+23)/[5(alpha+1)(alpha+3)(alpha+5)]. In alpha in (0,2], A5 switches sign exactly at alpha*=8-sqrt(41). The two-step odd recurrence from m=5, m=1 mod 4, proves A_(m+2)>0 and A_(m+4)>0 via lower bound 2alpha(4-2alpha)/[m(m+2+alpha)(m+4)(m+4+alpha)] for alpha<=alpha*; thus all n>=6 positive at and below the endpoint. Fourier Bochner criterion then proves PSD for all finite sets, and any consecutive sufficiently high positive frequencies form a Vandermonde system, so all finite sets of distinct points give strictly PD Gram matrices even when A5=0. Endpoints alpha=2 and alpha>2 are excluded as above.

## originality

PASS

Qualified best-of-knowledge: the exact c=pi/2 exponent cutoff 8-sqrt(41), all-frequency sign classification and unique vanishing fifth harmonic were not implied by the closely matching accessible primary statements. The foundational Gneiting generalized sine-power source explicitly poses the parameter question; Pólya convexity results cannot establish the nonconvex alpha>1 range; general strict-support criteria presuppose Fourier nonnegativity. A potentially relevant 1998 circle positivity paper was abstract-only and institutionally inaccessible, so historical priority remains an explicit risk rather than a fabricated NOT_COVERING finding.

## value

PASS

This is a natural, motivated slice of Gneiting's explicit generalized sine-power parameter question at support radius pi/2 (one quarter circumference, half the maximum intrinsic distance). It identifies the exact boundary of admissible nonconvex exponents, not just a numerical sample or low-order obstruction, by proving every remaining harmonic is nonnegative. The exact fifth-mode threshold and strict endpoint positive definiteness offer useful covariance-model and interpolation information, even without solving all radii or dimensions. The fact is independently meaningful and could be reused as a sharp test case in sphere/circle covariance theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
