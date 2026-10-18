# Independent mathematical audit

## correctness

PASS

PASS: For f(x)=x²/2,h=0 and arbitrary eps>0, central finite difference is x0=2eps exactly. H0=4, alpha=1/4 make first inner FISTA d0=−eps/2, with exact subproblem residual g+H0d0=0. The raw stop |d0|≤eps fires but the returned point has derivative 3eps/2>eps. All inequalities were independently checked with exact rational arithmetic for several positive eps and symbolically scale linearly, including Delta=eps/100≤eps/42 calculated from the quoted Theorem 3.3(i) radius bound and Lemma 2.4 step limit. Source-specific theorem conditions and algorithm printing were assessed from the assigned RESULT/REVIEW and primary abstract, but complete 2026 primary text was inaccessible; retain material risk of an omitted hypothesis or version revision; this C assessment is conditional on the literal printed source rules accurately transcribed in the audited package.

## originality

PASS

The broad warning about misusing raw small proximal-Newton steps is known and credited. The new precise finding is a source-specific contradiction to the literal zeroth-order framework: its exact first FISTA solve meets the cited radius hypothesis and published stopping test yet violates the same-epsilon stationarity claim. No inspected broad theorem supplies this source-specific parameter-compatible counterexample.

## value

PASS

PASS: A wrong ε-stationarity certificate for a newly proposed zeroth-order optimization algorithm is mathematically substantive even if the counterexample is scalar. Its exact first-step witness rules out finite-difference error and inner inexactness, identifies the cause, and gives the natural scaled stopping certificate from the cited Lemma 2.5. This directly corrects claimed guarantee semantics rather than merely pointing out a type issue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
