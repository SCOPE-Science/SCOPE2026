# Independent mathematical audit

## correctness

PASS

For ρ=x|ψ₀⟩⟨ψ₀|+y|ψ₁⟩⟨ψ₁|+z|ψ₂⟩⟨ψ₂| on the entire closed x+y+z=1 simplex, with ψ_i=(|0,i+1⟩−|1,i⟩)/√2, direct 8×8 qubit partial transpose splits into singleton x/2,z/2 and B₀=(1/2)[[0,−x],[−x,y]], B₁=(1/2)[[x,−y],[−y,z]], B₂=(1/2)[[y,−z],[−z,0]]. Sum of negative eigenvalue magnitudes gives the source exact formula; strict convexity in x,z for fixed y>0 forces x=z=(1−y)/2; y=0 has N=1/2. The reduced F(y)=(√(y²+(1−y)²)−y)/2+max(0,(3y−1)/4) decreases to y=1/3 and increases afterwards, yielding unique x=y=z=1/3 and (√5−1)/6; B₁ at optimum has zero eigenvalue and inertia (5,1,2). Independent full PT spectral checks on 861 sampled triples agree, but global theorem rests on convexity and derivative positivity, which was independently checked algebraically.

## originality

PASS

Johnston’s canonical 2×4 NPT-subspace construction and Rana’s universal negative-eigenvalue count bound are prior; neither controls trace norm/least sum of negative eigenvalues on this probability simplex. Chen–Đoković construct families with prescribed PT inertia; not equivalent to the quantitative minimum and unique optimizer. No matched Resultary finding of the exact sqrt5 minimax among these same three adjacent antisymmetric generators surfaced. Originality remains bounded by possible obscure quantum negativity optimization reports.

## value

PASS

The canonical maximal-NPT 2×4 subspace is a natural geometry object, and minimal negativity quantifies robustness of entanglement on its diagonal-state simplex, beyond existence of NPT or inertia bounds. The unique uniform minimizer unexpectedly lies on an inertia boundary, explicitly distinguishing trace magnitude from maximal negative-eigenvalue count. The result is self-contained and quantitatively useful despite finite dimensionality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
