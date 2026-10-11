# Review
## Correctness
**PASS.** The sign follows without a modeling assumption beyond the coefficients printed by Wen--Liu--Lu. Their \(\beta_1\) coefficient of the first parameter is negative, while the multiplier \(b^4/a^3\) is strictly positive. High-precision replay of the displayed decimal constants reproduces the magnitude and sign of the scaled coefficient. A separate check from \(4\bar\beta_1-\bar\beta_2^2=0\) recovers the source's displayed saddle-node polynomial and its tangent \(\bar\lambda_1=62.4500798\ldots\,\bar\lambda_2\). The opposite sign printed in equation (16) reverses that tangent. Risk is limited to the precision of the source's intermediate rounded coefficients; the sign itself is unaffected.

## Originality
**PASS.** The source's full \(BT_2\) derivation, Theorem 5.1, publisher record, cited Bogdanov--Takens reference, targeted public searches for corrections/errata and distinctive coefficients, a semantic literature index, and public indexed comparison records were compared by implication rather than title. No checked source states the equation-(16) sign correction or a stronger source-specific statement. Generic Bogdanov--Takens theory supplies the framework but cannot imply which of the paper's two contradictory source-specific signs is the intended numerical coefficient without inspecting this calculation. Residual risk is an unindexed author correction or informal note.

## Value
**PASS.** Equation (16) is the paper's explicit local reduced system at \(BT_2\). Using its printed sign literally reverses the saddle-node tangent in the physical parameter plane and makes the normal form incompatible with the theorem's own saddle-node and homoclinic curves. Correcting the sign therefore matters for reproducibility and for deciding which local parameter side corresponds to each reduced regime; it is not merely typographic punctuation. The finding is intentionally limited to that correction because the downstream curves already appear to have used the correct sign.

## Closest literature and limitations
The closest methodological source is Carrillo--Verduzco--Delgado (2010), which treats parameterized Bogdanov--Takens reductions generally; it does not contain these neuron-model coefficients. The closest public indexed findings concern other sign inconsistencies or different neuron normal forms and do not imply this claim. The result does not certify the full center-manifold computation or the global bifurcation diagram.

Same-model review: passed. Independent audit: not yet performed.
