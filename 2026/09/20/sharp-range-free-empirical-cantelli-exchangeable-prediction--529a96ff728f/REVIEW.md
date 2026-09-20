# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The central leave-one-out identity was rederived directly. For a
deterministic vector of length \(M=n+1\), full-sample normalized coordinates
\(u_i\) satisfy \(\sum u_i=0\) and \(\sum u_i^2=M\), while the deleted-point
studentized residual obeys
\[
T_i^2=\frac{M(M-2)u_i^2}{(M-1)(M-1-u_i^2)}.
\]
The map is sign-preserving and monotone in \(|u_i|\), giving the exact
threshold
\[
a_n(t)^2=\frac{n^2t^2}{n^2-1+nt^2}.
\]

The deterministic one-sided count inequality
\[
\#\{i:u_i\ge a\}\le\left\lfloor\frac{M}{1+a^2}\right\rfloor
\]
follows from one Cauchy--Schwarz step after separating the threshold
coordinates from their complement. Its strict-threshold counterpart is
\(\#\{i:u_i>a\}\le\lceil M/(1+a^2)\rceil-1\).
Exchangeability then converts the samplewise count into the desired
probability bound without any distributional moment or support assumption.

Sharpness was checked algebraically. A uniformly permuted two-level vector
with \(r\) positive coordinates has
\[
T_{\rm high}^2=
\frac{(M-2)(M-r)}{(M-1)(r-1)}
\]
for \(r\ge2\), and \(+\infty\) for the unique high coordinate when \(r=1\).
Thus \(T_{\rm high}\ge t\) is equivalent to \(r\le R_n(t)\); choosing
\(r=\lfloor R_n(t)\rfloor\) or
\(r=\lceil R_n(t)\rceil-1\) attains the inclusive or strict bound,
respectively.

A standalone exact-rational verification artifact checks the algebraic
identity \(R_n(t)=(n+1)/(1+a_n(t)^2)\), the extremizer inequalities, and
the next-integer failures for \(2\le n\le80\) over 11 rational values of
\(t^2\), including the \(n=20\) prediction example. All 869 parameter
cases pass.

## Originality

PASS, to the best of our knowledge. Saw, Yang and Mo (1984) established
the empirical two-sided Chebyshev line under exchangeability, and
Stellato, Van Parys and Goulart (2017) treated a multivariate extension.
Troffaes and Basu (2019) is the closest source found: it explicitly seeks
a one-sided Cantelli counterpart for the same future-observation/sample-
mean/sample-standard-deviation setup. Its theorem inserts a
range-dependent positive correction and assumes boundedness. The paper
states that the authors had not found a way to avoid the correction, and
its discussion again identifies that offset as the critical difference
from the earlier empirical Chebyshev bound.

Troffaes--Basu Lemma 7 already provides the deterministic one-sided count
inequality in an equivalent form, so that ingredient is not claimed as
new. The contribution assessed here is the exact monotone transformation
from the externally studentized prediction residual to the full-sample
standardized coordinate, which eliminates the correction, plus the exact
finite-sample staircase and sharp orbit extremizers.

Searches through the present for combinations of “Cantelli”,
“exchangeable”, “sample standard deviation”, “studentized prediction”,
“one-sided prediction interval”, “range correction”, and the cited
authors did not identify a later source with this formula or a removal of
the 2019 correction.

The strongest residual originality risks are older prediction-interval
literature and inaccessible details of two papers. Konijn (1987) concerns
distribution-free prediction intervals derived from the Saw--Yang--Mo
line, but its full text could not be inspected. The one-page 1988
Saw--Yang--Chin correction was identified bibliographically but its
mathematical content was not inspected. These are concrete residual risks,
not evidence of coverage. The fact that Troffaes and Basu explicitly
identified correction removal as unresolved in 2019 weighs against, but
does not logically exclude, an older equivalent formula under different
terminology.

## Value

PASS. The result converts a previously range-corrected, bounded-support
one-sided inequality into an exact support-free theorem under the same
minimal structural assumption as the empirical Chebyshev inequality:
finite exchangeability. It also supplies exact extremizers and the finite-
sample integer staircase rather than only an asymptotic Cantelli limit.

The prediction interpretation is direct. For example, \(n=20\) and
\(t=19/\sqrt{20}\) give a sharp strict-tail error of \(1/21\), so a
closed one-sided interval \(( -\infty,\bar X_n+tS_n]\) has at least
\(20/21\) coverage for every exchangeable law. The theorem also shows the
unavoidable \(1/(n+1)\) granularity of finite-multiplier prediction under
exchangeability alone.

## Scientific limitations

The result is an unconditional exchangeable prediction statement. It does
not produce a conditional distribution-free p-box for \(X_{n+1}\) after
conditioning on the realized numerical values of \(\bar X_n\) and \(S_n\);
that stronger problem is distinct.

The extremal orbit laws need not be iid. Therefore sharpness is over the
exchangeable class, although the inequality itself automatically applies
to iid samples. No claim is made that the same staircase is sharp within
the iid subclass.

Exact attainment uses an extended convention when a leave-one-out sample
variance vanishes. If one requires \(S_n>0\) almost surely, the inequalities
remain valid, while some staircase endpoint constructions may require
arbitrarily close perturbations rather than the displayed two-level
extremizer.
