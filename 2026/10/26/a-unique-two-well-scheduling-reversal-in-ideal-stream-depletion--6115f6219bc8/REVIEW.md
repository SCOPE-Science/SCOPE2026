# Review of the two-well endpoint stream-depletion ordering theorem

## Correctness — PASS

The step-response model \(K_i(t)=\operatorname{erfc}(\alpha_i/\sqrt t)\) and pulse superposition yield an exact difference \(Q[G(z)-G(rz)]\). The derivative of \(G\) changes sign at exactly \(z_0=\sqrt{3\log2}\), so the difference has one zero for each \(r>1\). The derivative signs at that zero establish strict parameter monotonicity, and the zero of \(G\) supplies the limiting threshold. All model assumptions, endpoint conventions, equality cases, and asymptotics are explicit. The program executed with 5,000 parameter draws and 999 ratio-pair comparisons; these finite tests are not substituted for proof.

## Originality — PASS with residual risk

Published mathematical searches and available related records did not establish an equivalent two-well equal-duration endpoint order theorem. The Glover–Balmer kernel and Jenkins pulse superposition are foundational, not new. The 2007 accessible Miller et al. full-text analysis concerns semianalytical depletion response curves and aquifer boundaries rather than this exact scheduling comparison. Wallace–Darama–Annable (1990) treats cyclic pumping of a well, and Bredehoeft–Kendy (2007 online) concerns seasonal offsets by pumping and recharge. Their complete texts were not available; broader prior statements could imply this result. Search absence is not proof of worldwide uniqueness.

## Mathematical value — PASS

Stream managers may need to minimize instantaneous river depletion at a specified end-of-operation low-flow date while meeting a fixed total two-well extraction schedule. The result provides a universal, computable *sharp duration policy boundary* rather than a simulation-specific comparison. Its strict transition law, dimensionless distance dependence, and sharp limiting range explain exactly when the natural near-first intuition fails. It is limited to the idealized, transparently specified physical setting.

Self-review: passed. Independent audit: not yet performed.
