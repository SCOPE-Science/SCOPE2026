# Independent mathematical audit

## correctness

PASS

I recovered the two rank invariants on the 16-dimensional regular module. For nonzero linear part write a=e₁v+c with v a unit in B=Λ⟨e₂,e₃,e₄⟩. Multiplying a on the right by v⁻¹ does not change aE. For a′=e₁+u+w, projection to e₁B gives eight independent images from B, and a′e₁b=a′(u−w)b because (u+w)(u−w)=0 in B. Thus r₁=8, also in characteristic two. The correct sign explanation of the displayed square is that odd–odd cross terms cancel, whereas odd–even terms commute and contribute 2ℓ∧ω in degree three; the remaining square term is ω². The frozen explanatory sentence reversing this sign rule is a slip, not an error in the square identity or tables. The degree-three image of a² on 1 and its degree-four image on V give r₂=2 when ℓ∧ω≠0 in odd characteristic; if ℓ≠0 and ℓ∧ω=0, ω=ℓ∧z and r₂=0. When ℓ=0 and ω≠0, filtration gives r₁=2+rank(ω∧−|V), namely 4 or 6 by the alternating normal forms, with r₂=1 only for rank four in odd characteristic. Higher leading degrees give r₁=2,1,0; all cubes are zero. The formula (b₃,b₂,b₁)=(r₂,r₁−2r₂,16−2r₁+r₂) then gives the partitions. A fixed nonzero ℓ leaves q³ two-forms in its wedge kernel, and (q−1) times the number of two-planes counts the nonzero decomposable forms, giving all the multiplicities after allowing the q⁵ higher-degree terms. These arguments apply over extension fields. I inspected artifacts/verify.py and VERIFICATION.md without executing the uploaded code: selected ranks are checked by elimination, whereas the exhaustive binary histogram uses the structural predictor rather than independent ranks on all 32,768 elements.

## originality

PASS

The distinct claim is the all-radical finite-field distribution including inhomogeneous multipliers in both characteristics. Homogeneous form counts and some rank strata are prior ingredients. A later indexed full-algebra theorem does reproduce the radical tables exactly; it is not evidence of prior coverage based on the available chronology.

## value

PASS

Four generators are the first exterior dimension with nondegenerate bivectors and enough higher grades to distinguish the mixed-degree contribution to the square from the Pfaffian contribution. The entire regular-module histogram distinguishes two ways of producing size-three blocks in odd characteristic and their collapse in characteristic two. It is a useful exact finite-field benchmark beyond homogeneous orbit counts or a generic Jordan type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
