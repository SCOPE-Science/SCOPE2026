# Same-model review

## Correctness

**PASS.** The algebraic reduction is exact: after nonzero row/column scaling and discrete logarithms in the cyclic group \(\mathbb F_9^*\cong\mathbb Z_8\), nonvanishing of every \(2\times2\) minor is equivalent to pairwise distinct coordinate differences between every two exponent rows. Thus a hypothetical size-seven strong-AONT defining matrix yields a \(\operatorname{CDPA}(7,7;8)\).

The supporting extremal claim is verified after a complete normalization. There are exactly 5040 possible normalized nonzero rows. After fixing one nonzero row, column symmetry reduces it to one of seven canonical missing-residue cases. In every case the compatibility graph has 64 vertices, 24 edges, and no triangle, excluding five rows. An explicit four-row witness proves sharpness. The standalone artifact separately verifies these counts and the published six-by-six \(\mathbb F_9\) lower-bound matrix.

## Originality

**PASS, to the best of our knowledge.** Nasr Esfahani and Stinson explicitly state \(6\le M_R([1,2],9)\le7\), so the size-seven exclusion closes a documented one-unit gap. Searches were carried out under strong AONT, range AONT, all-or-nothing transform, difference matrix, difference packing array, cyclic difference packing array, CDPA, and the exact parameters involved. No later source resolving \(M_R([1,2],9)\) or proving nonexistence of \(\operatorname{CDPA}(5,7;8)\) was located.

The most relevant older sources are Jianxing Yin's 2004 paper introducing difference packing arrays (DOI 10.1360/03ys0037) and 2005 paper on cyclic difference packing and covering arrays (DOI 10.1007/s10623-004-3991-3). Their accessible abstracts and indexed descriptions were inspected. The 2005 abstract gives the even-order column bound and four-row constructions but does not state the row-maximality result used here. Their full texts were not inspected, so there remains a concrete residual risk that a small-parameter classification or an equivalent obstruction appears there.

## Value

**PASS.** The result closes the only unresolved value in the small-odd-alphabet list of Theorem 3.11 of the range-AONT paper and supplies an exact extremal statement for the cyclic difference-packing object that causes the obstruction. The reduction also explains structurally why the remaining AONT parameter fails, rather than merely reporting a direct matrix search.

## Scientific limitations

The CDPA nonexistence proof is computer-assisted after an exact finite symmetry reduction and currently addresses only the parameter pair \((n,q)=(7,8)\). No general row bound for \(\operatorname{CDPA}(k,q-1;q)\) is claimed. The AONT conclusion is for linear strong AONTs and does not imply a corresponding nonlinear nonexistence result. The two older Yin papers identified above remain residual originality risks because their full texts were not inspected.

Same-model review: passed. Independent audit: not yet performed.
