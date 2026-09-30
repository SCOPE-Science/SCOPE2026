# Independent audit — 2026-09-29 UTC

Record: `2026/09/20/infinitary-harmonic-four-i-components--0182bc176f0b`  
Assigned source tree: `32a42397a7f1c0fccde97fd0da5d64ffe57c7806`  
Audited current source tree: `32a42397a7f1c0fccde97fd0da5d64ffe57c7806`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `7a145550c9c888ca64972fe0f37a0ca252ec42ef`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The four-I-component classification is complete. The Hagis-Cohen mean bound restricts the integer mean to 6,...,15. At each partial choice, monotonicity of rho(x)=x/(x+1) gives a rigorous finite upper bound for the next ordered I-component; after three choices the fourth is uniquely t/(1-t). An independent exact-rational enumeration reproduced the successive bounds 61, 765 and 131070, all 48,733 three-component branches, 289 integral final candidates and exactly the six solutions 270, 420, 630, 9100, 46494 and 646425 with the displayed component tuples and harmonic means. The largest integral final candidate is 2^32-1, so the deterministic primality/power test is comfortably within the claimed range.

## Originality

**qualified_supported_exact_boundary_extension**. Hasanalizade's 2026 paper was inspected at Lemma 2.3: it explicitly classifies J<=3 as {1,6,45,60,90,15925} and then proceeds to upper bounds for J>=4 rather than classifying J=4. Hagis-Cohen's foundational work establishes fixed-J finiteness and historical bounded data; OEIS independently lists the six values but does not provide a J=4 completeness proof. Searches did not locate a prior exact four-component classification. The novelty claim is therefore supported as a proof of completeness, not as discovery of the individual numerical values already present in historical data.

## Scientific value

**meaningful_exact_classification**. The result advances the published exact small-component boundary from J<=3 to J<=4 and replaces bounded tables with a proved finite exhaustive search. It also provides a reusable residual-product enumeration method.

## Independent checks

- Reimplemented the exact residual-product search independently of the repository script.
- Verified all six harmonic means as exact rational identities.
- Inspected Hasanalizade 2026 Lemma 2.3 directly and checked current OEIS corroboration.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/infinitary-harmonic-four-i-components--0182bc176f0b
- https://doi.org/10.1017/S0004972700017949
- https://doi.org/10.1017/S0004972726101324
- https://doi.org/10.1090/S0025-5718-1990-0993927-5
- https://oeis.org/A063947
- https://oeis.org/A361385

## Limitations

- The classification stops at exactly four I-components and says nothing complete for J>=5.
- The completeness proof is computer-assisted, though every search bound and arithmetic test is exact.
- The individual values were already visible in historical tables/data; the contribution is the exact J=4 completeness theorem.
- No formal proof-assistant certificate is provided.
