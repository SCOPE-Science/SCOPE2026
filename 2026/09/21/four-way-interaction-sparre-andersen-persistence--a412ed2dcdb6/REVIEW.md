# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. Walsh-Fourier expansion on the four-dimensional sign cube shows that fair 3-wise independence kills every nonconstant coefficient except the fourth-order product moment `theta`; hence the sign law is exactly `2^-4(1+theta prod e_i)`. This also proves that every proper sign marginal is iid and that the full sign law is exchangeable.

For positive iid amplitudes supported in `[a,b]` with `b<2a`, every three-term partial sum with a 2-to-1 sign majority has the majority sign. The remaining equality-of-count cases reduce to two elementary exchangeability calculations: two iid non-atomic pair sums compare with probability `1/2`, and for iid continuous symmetric differences `D_1,D_2`, `P(D_1>0,D_1+D_2>0)=3/8`. Pattern enumeration then gives positive-parity persistence `15/64` and negative-parity persistence `5/16`. Their affine mixture gives `(35-5 theta)/128`; at `theta=0` this is `35/128`, matching the classical iid Sparre-Andersen value.

The exact verification artifact checks all one-, two-, and three-sign marginals for both parity classes and the rational arithmetic of the endpoint values, separation, midpoint and affine coefficient.

## Originality

PASS, to the best of our knowledge, with a deliberately narrow claim.

Checked prior work establishes nearby facts that are not claimed as new. Sparre Andersen gives the classical iid fluctuation law and dependent/exchangeable fluctuation identities. Berger-Béthencourt extend the persistence statement to exchangeable, sign-invariant vectors. Iľkovič-Yan determine extremal persistence bounds within that sign-invariant class. Benjamini-Kozma-Romik explicitly use product/parity conditioning to construct k-wise independent random walks with nonclassical behavior, so the dependence gadget is old. Narayanan studies maximal displacement under 3-wise independence.

Searches for combinations of “Sparre Andersen”, “3-wise/three-wise/k-wise independent”, “persistence”, “first passage”, “limited independence”, the exact constants `15/64`, `5/16`, `35/128`, and links between the limited-independence random-walk literature and Sparre-Andersen persistence did not locate the present finite-horizon formula. The novelty claim is therefore only the exact response `(35-5 theta)/128` of persistence to the sole fourth-order sign interaction and the resulting two continuous exchangeable laws with identical every-proper-subset distributions but distinct persistence.

Residual risk remains because older dependent-fluctuation literature is extensive and equivalent statements may use different language. The full text of Sparre Andersen's 1953 Scandinavian Actuarial Journal paper was not inspected in full; its abstract was checked and it is scientifically the most plausible older source among those found that could contain an equivalent dependent-fluctuation observation. This uncertainty does not provide concrete evidence of prior coverage.

## Value

PASS. The result isolates a sharp conceptual boundary around modern exchangeable/sign-invariant Sparre-Andersen extensions. Exchangeability plus continuous symmetric marginals plus the strongest possible proper-subset independence at horizon four still does not recover universal persistence. The exact fourth-order coefficient makes the missing information explicit and measurable.

## Limitations

The result is finite-horizon. The clean constants use an independent sign-amplitude representation with a positive non-atomic amplitude supported in a ratio-`<2` interval. The theorem does not characterize all 3-wise independent real-valued increment laws or asymptotic persistence. The parity construction and Walsh-Fourier representation are classical. No independent audit has yet been performed.
