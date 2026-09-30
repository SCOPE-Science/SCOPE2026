# Independent audit — 2026-09-28

Record: `2026/09/10/043`  
Audited tree: `aed93a6ffced1964584297eb58347e8002476a59`  
Disposition: **passed**

## Correctness
I checked the constants against Evra–Kaufman v3. Remark 3.4 gives the stated `mu`, `epsilon`, and local `bar-epsilon` formulas. At `d=3`, `C0=1/960` and `C1=160`. For a relevant proper link, take a minimum-weight vertex `v`; its singleton 0-cochain has class norm `w(v)`, while Lemma 2.3 gives `||Gamma^1({v})||=2w(v)`, hence `Exp_b^0 <= 2`. Thus any common local parameter satisfies `beta <= 2`. The exact substitutions are

- `bar-epsilon <= (1/3)(2/160)^3 = 1/1536000`,
- `mu <= ((2/160)^3/960)^16 = (1/491520000)^16 < 10^-139`,
- `epsilon <= mu`.

So the published criterion cannot certify `0.08` at `d=3`. The record correctly does **not** claim that the underlying complex cannot have expansion `>=0.08` by some other proof.

## Originality
The source paper contains the parametric formulas but does not state this `d=3` cap or compare it to `0.08`. I did not locate a prior source making this exact feasibility deduction. This is a useful new application/diagnostic of known formulas rather than a new local-to-global theorem.

## Scientific value
The result is valuable as a route-elimination certificate: it saves future work from trying to meet an impossible numerical target with the published constants while leaving alternate approaches open.

## Limitations
The conclusion is method-specific.

## Sources
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/043
- https://arxiv.org/abs/1510.00839
- https://arxiv.org/html/1510.00839v3
