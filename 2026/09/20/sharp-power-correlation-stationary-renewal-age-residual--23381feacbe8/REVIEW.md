# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The proof reduces the stationary recurrence pair to the standard representation
\((A,R)=(UL,(1-U)L)\) with a uniform split independent of the size-biased interval length.
The three required moments are then beta integrals. The dependence on the renewal law is
through the single dimensionless ratio
\(Q_r=(E X^{r+1})^2/(E X\,E X^{2r+1})\), which lies in \((0,1]\) by Cauchy--Schwarz.
The resulting fractional-linear correlation is strictly decreasing in \(Q_r\), giving
both endpoint constants. The two-point construction realizes every \(Q_r\in(0,1]\),
so the stated range is genuinely sharp rather than only bounded. Boundary cases,
integer specializations, the exponential zero-correlation benchmark and large-r
asymptotics were checked separately.

## Originality

PASS, to the best of our knowledge, with a specific residual risk. The ordinary
\(r=1\) correlation is old and is explicitly excluded from the novelty claim. The
Schur-constant radial-uniform representation is also old; Nelsen (2005) and Nair--Sankaran
(2014) are direct predecessors. Losidis--Politis--Psarrakos (2021) treats joint tails and
moments of recurrence times, so raw mixed moments are likewise not claimed as new.

Searches were made for combinations of backward/forward recurrence time, age/residual
life, Schur-constant and \(\ell_1\)-norm symmetric distributions with power correlation,
transformed correlation, mixed moments, beta-function formulas, and equivalent Dirichlet
radial formulations. No source located the all-r sharp Pearson-correlation interval,
full attainability, or its endpoint classification. The closest broad review found was
Lefèvre--Simon (2021), which surveys Schur-constant/Dirichlet/Archimedean links. Its full
text was not completely inspected, so it is the most important residual bibliographic
risk, together with Nelsen (2005), whose abstract explicitly mentions correlation
coefficients but whose complete text was not available in the sources inspected.

## Value

PASS. The result converts the classical single linear-correlation range into a full
nonlinear identification theorem valid for every positive power. It identifies exactly
how much Pearson dependence can remain after nonlinear power transformation, proves all
intermediate values feasible, singles out deterministic and exponential renewal laws,
and shows a universal high-power collapse independent of the interarrival family.

## Scientific limitations

The theorem is stationary, concerns equal positive powers and Pearson correlation, and
does not address unequal powers or finite-time recurrence pairs. Its upper endpoint is a
sharp supremum, not an attained maximum. Priority remains subject to the residual older
Schur-constant-literature risk described above.
