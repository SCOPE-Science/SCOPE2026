# Independent mathematical audit

## correctness

PASS

For N>=4 the two exterior bonds are distinct and the internal bond is unchanged; subtracting the two energies gives exactly the displayed non-descent criterion. A trace term specifies the triple at the labelled origin and each subsequent overlap, hence counts each labelled cyclic word once, even for nonprimitive words. The AAA and ABB rows give (1,q-1,0,0,0); AAB allows every appended colour, ABA only its last colour, and ABC forbids the middle colour. This gives the stated quotient and the binary deletion. Setting a=q-1, b=q-2, elimination in tI-M gives t times [t^2(t-1)(t-b)-a((1+t)(t-b)+tb)], the stated quartic, and binary block determinant t(t^3-t^2-t-1). Appending b,b from (u,a,b), then a new constant colour three times and the desired two other symbols, proves strong connectivity; all-equal self-loops give primitivity. The uniquely normalized Perron vector is constant on colour orbits; the trace sums eigenvalue powers with algebraic multiplicity, so the Perron coefficient is one. The proof covers fixed q and all populations, not a single sector or neutral-move dynamics. RESULT.md lines 42–52 checked analytically; artifacts/verify.py lines 7–127 inspected, not executed. Its finite checks are diagnostic, not the basis for the all-N proof.

## originality

PASS

The supported distinct finding is the complete all-colour uniform nearest-neighbour ferromagnetic labelled-ring count and its quartic growth law for q>=3. The binary forbidden-word baseline and standard transfer-matrix method are not independent novelty claims. There is a materially close Potts precedent in Dhar that should be cited specifically, but the retrieved passage does not furnish the claimed classification or entropy law.

## value

PASS

The model and the total metastable-state entropy are natural before calculation. A uniform five-pattern structural reduction and a closed quartic for arbitrary q replace a q^3-state computation; a researcher can compare colour effects or use the exact labelled finite count without running the dynamics. This is more than re-counting the known binary blocked words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
