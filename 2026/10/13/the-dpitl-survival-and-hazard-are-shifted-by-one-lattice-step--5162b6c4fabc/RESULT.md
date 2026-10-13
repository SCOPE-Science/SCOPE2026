# The DPITL survival and hazard are shifted by one lattice step
## Finding
For the discrete power inverted Topp–Leone (DPITL) distribution, let
\[
S_c(w)
=
\left[
\frac{1+2w^\eta}{(1+w^\eta)^2}
\right]^\kappa,
\qquad
\kappa,\eta>0,
\qquad
w\in\mathbb N_0.
\]
The source constructs the discrete PMF by survival discretization:
\[
p_w
=
\Pr(W=w)
=
S_c(w)-S_c(w+1).
\]
It also gives the CDF
\[
F(w)
=
\Pr(W\le w)
=
1-S_c(w+1).
\]

These two correct formulas determine the discrete survival events exactly:
\[
\boxed{
\Pr(W\ge w)=S_c(w)=1-F(w-1)
}
\]
and
\[
\boxed{
\Pr(W>w)=S_c(w+1)=1-F(w).
}
\]

Equation (4) of the source instead labels
\[
S_c(w+1)
\]
as
\[
\Pr(W\ge w).
\]
That is a one-lattice-step error: the displayed quantity is the strict survival \(\Pr(W>w)\), not the inclusive survival \(\Pr(W\ge w)\).

The source then defines its hazard by
\[
\psi_{\mathrm{pub}}(w)
=
\frac{p_w}{S_c(w+1)}.
\]
The proper discrete hazard probability is
\[
\boxed{
h(w)
=
\Pr(W=w\mid W\ge w)
=
\frac{p_w}{S_c(w)}
=
1-\frac{S_c(w+1)}{S_c(w)}.
}
\]
Because
\[
p_w=S_c(w)-S_c(w+1),
\]
the source quantity satisfies
\[
\boxed{
\psi_{\mathrm{pub}}(w)
=
\frac{h(w)}{1-h(w)}.
}
\]
It is therefore the odds corresponding to the true hazard probability, not the hazard probability itself.

This distinction is substantive because the printed “hazard” can exceed one. At the first lattice point,
\[
S_c(0)=1,
\qquad
S_c(1)=\left(\frac34\right)^\kappa,
\]
so
\[
\boxed{
h(0)
=
1-\left(\frac34\right)^\kappa
}
\]
but
\[
\boxed{
\psi_{\mathrm{pub}}(0)
=
\left(\frac43\right)^\kappa-1.
}
\]
For
\[
\kappa=3,
\]
these values are
\[
h(0)=\frac{37}{64}=0.578125
\]
and
\[
\psi_{\mathrm{pub}}(0)=\frac{37}{27}=1.370370\ldots.
\]
A conditional failure probability cannot exceed one.

The same one-step shift propagates into the probability-generating function. For any nonnegative integer-valued random variable with inclusive survival
\[
S_w=\Pr(W\ge w),
\]
summation by parts gives
\[
G(t)
=
\mathbb E[t^W]
=
1+(t-1)\sum_{w=1}^{\infty}t^{w-1}S_w.
\]
Therefore the DPITL PGF is
\[
\boxed{
G(t)
=
1+(t-1)
\sum_{w=1}^{\infty}
t^{w-1}S_c(w).
}
\]
The source's Eq. (6) writes the correct abstract identity but then substitutes
\[
S_c(w+1)
\]
from its shifted Eq. (4). Hence the displayed series is not the PGF of the PMF in Eq. (2).

Whenever the mean is finite,
\[
\mathbb E[W]
=
\sum_{w=1}^{\infty}S_c(w).
\]
The source's Eq. (9) instead gives
\[
\sum_{w=1}^{\infty}S_c(w+1).
\]
Thus the mean error is exactly
\[
\boxed{
\mathbb E[W]-\mu_{\mathrm{pub}}
=
S_c(1)
=
\left(\frac34\right)^\kappa.
}
\]

For the admissible parameter pair
\[
(\kappa,\eta)=(3,1),
\]
the defining PMF gives
\[
\boxed{
\mathbb E[W]
=
0.8327998896188664\ldots
}
\]
whereas Eq. (9) gives
\[
\boxed{
\mu_{\mathrm{pub}}
=
0.4109248896188664\ldots.
}
\]
Their difference is
\[
\frac{27}{64}=0.421875.
\]

Accordingly, the source's HRF plots and the PGF-derived moment formulas do not correspond to the DPITL PMF as defined unless the missing lattice step is restored.

## Assumptions and scope
The parameter domain is
\[
\kappa>0,
\qquad
\eta>0,
\]
and the support is
\[
\mathbb N_0=\{0,1,2,\ldots\}.
\]

The finding distinguishes two standard discrete tail events:
\[
\Pr(W\ge w)
\]
and
\[
\Pr(W>w).
\]
The source's Eq. (3) correctly identifies
\[
1-F(w)=\Pr(W>w)=S_c(w+1).
\]
The error occurs when Eq. (4) reuses that quantity as \(\Pr(W\ge w)\).

The mean comparison is stated only when the mean is finite. The numerical example
\[
(\kappa,\eta)=(3,1)
\]
lies safely in that regime because
\[
S_c(w)=O(w^{-3}),
\]
so the survival sum converges.

The finding does not challenge the PMF in Eq. (2) or the CDF in Eq. (3). It corrects downstream survival, hazard, PGF, and moment formulas derived from them.

## Proof
From
\[
p_w=S_c(w)-S_c(w+1),
\]
telescoping gives
\[
\sum_{j=w}^{\infty}p_j
=
S_c(w),
\]
because
\[
S_c(j)\to0.
\]
Hence
\[
\Pr(W\ge w)=S_c(w).
\]

Similarly,
\[
\Pr(W>w)
=
\sum_{j=w+1}^{\infty}p_j
=
S_c(w+1).
\]
Since the source's CDF is
\[
F(w)=1-S_c(w+1),
\]
this also confirms
\[
1-F(w)=S_c(w+1).
\]

The correct hazard is the conditional probability
\[
h(w)
=
\frac{\Pr(W=w)}{\Pr(W\ge w)}
=
\frac{S_c(w)-S_c(w+1)}{S_c(w)}.
\]
The source instead divides by \(S_c(w+1)\). Therefore
\[
\psi_{\mathrm{pub}}(w)
=
\frac{S_c(w)-S_c(w+1)}{S_c(w+1)}.
\]
Writing
\[
q_w=\frac{S_c(w+1)}{S_c(w)},
\]
one has
\[
h(w)=1-q_w
\]
and
\[
\psi_{\mathrm{pub}}(w)
=
\frac{1-q_w}{q_w}
=
\frac{h(w)}{1-h(w)}.
\]

For the PGF,
\[
p_w=S_w-S_{w+1}
\]
with
\[
S_w=\Pr(W\ge w).
\]
Then
\[
\sum_{w=0}^{\infty}t^wp_w
=
\sum_{w=0}^{\infty}t^wS_w
-
\sum_{w=0}^{\infty}t^wS_{w+1}.
\]
Using
\[
S_0=1
\]
and shifting the second sum gives
\[
G(t)
=
1+(t-1)
\sum_{w=1}^{\infty}t^{w-1}S_w.
\]
For DPITL,
\[
S_w=S_c(w),
\]
not \(S_c(w+1)\).

Finally, differentiating at
\[
t=1
\]
or using the tail-sum identity yields
\[
\mathbb E[W]
=
\sum_{w=1}^{\infty}S_c(w).
\]
Subtracting the source's shifted series
\[
\sum_{w=1}^{\infty}S_c(w+1)
\]
leaves only
\[
S_c(1).
\]

## Verification
The included checker implements the source's continuous survival sequence,
\[
S_c(w)
=
\left[
\frac{1+2w^\eta}{(1+w^\eta)^2}
\right]^\kappa,
\]
and the PMF
\[
p_w=S_c(w)-S_c(w+1).
\]

It checks telescoping numerically, verifies that
\[
p_w/S_c(w)
\]
lies in the probability range, and confirms the exact odds relationship
\[
p_w/S_c(w+1)
=
h(w)/(1-h(w)).
\]

At
\[
\kappa=3,
\]
the checker obtains
\[
h(0)=37/64
\]
and
\[
\psi_{\mathrm{pub}}(0)=37/27>1.
\]

For
\[
(\kappa,\eta)=(3,1),
\]
the checker computes the mean independently from the PMF and from the correct survival sum, verifies their agreement, evaluates the shifted source series, and confirms the exact difference
\[
27/64.
\]

It also compares the direct PMF PGF at an interior value of \(t\) with the correct survival-sum identity and with the source's shifted series. The direct PGF agrees with the corrected identity and not with the shifted one.

## Relationship to prior work
Hassan et al. construct the DPITL law by survival discretization. Their Eq. (2) correctly defines
\[
p_w=S_c(w)-S_c(w+1),
\]
and Eq. (3) correctly states
\[
F(w)=1-S_c(w+1).
\]
Equation (4) then changes the meaning of \(S_c(w+1)\), labeling it as
\[
\Pr(W\ge w),
\]
and uses it as the hazard denominator.

The inconsistency can therefore be established entirely from consecutive formulas in the source. It is not a disagreement over the continuous PITL parent law.

The earlier continuous PITL article defines the continuous survival used for discretization but does not address this discrete lattice indexing. The earlier discrete inverted Topp–Leone literature provides background on survival discretization but does not supply a correction of the 2026 DPITL equations located in the searches performed here.

Focused searches using the exact DOI, DPITL name, survival-function terminology, hazard-rate aliases, PGF language, and one-step lattice-shift formulations did not locate a published corrigendum or an equivalent model-specific correction.

A separate result on the same 2026 source classifies its power-law tail and moment-existence thresholds. That statement does not imply the present indexing correction: the PMF can have the stated tail behavior while the source's survival, hazard, and PGF formulas remain shifted by one lattice point.

## Limitations
The finding corrects the printed analytic formulas. It does not establish which formulas were used in unpublished software that produced every figure or simulation result.

Only the first raw moment is quantified explicitly here. Higher PGF-derived factorial and raw moments are also affected by the shifted PGF, but their complete correction formulas are not needed for the accepted claim.

The paper's estimation procedures that use the PMF directly are not automatically invalidated by this indexing error.

## References
1. A. S. Hassan, E. A. Seyam, A. A. Alzahrani, and O. A. Saudi, “An innovative discrete distribution for modeling genotoxicity data: Applications in pharmacology and environmental health,” AIMS Mathematics 11 (2026), 1145–1174. DOI: 10.3934/math.2026049.
2. T. A. Abushal, A. S. Hassan, A. R. El-Saeed, and S. G. Nassr, “Power Inverted Topp–Leone Distribution in Acceptance Sampling Plans,” Computers, Materials & Continua 67 (2021), 991–1011. DOI: 10.32604/cmc.2021.014620.
3. A. S. Eldeeb, M. Ahsan-Ul-Haq, and A. Babar, “A discrete analog of inverted Topp-Leone distribution: properties, estimation and applications,” International Journal of Analysis and Applications 19 (2021), 695–708. DOI: 10.28924/2291-8639-19-2021-695.
