# Independent mathematical audit

## correctness

PASS

For the adjacency quantum walk on C10, independently reconstructed all ten exact eigenvalues as a_j+b_j*phi, phi=(1+sqrt(5))/2. The DFT of each displacement probability has F_k=(1/10)sum_j exp(i[(a_j-a_{j-k})x+(b_j-b_{j-k})y]). An independent exact symbolic search obtains counts at (0,0),(1,-2),(-1,2) of (0,0,0) for every odd nonzero k and (2,2,2) for k=2,4,6,8. The normalized torus density (1-cos(x-2y))/(4pi^2) has moments 1,-1/2,-1/2 exactly at these characters and no other nonzero moments; each F_k expectation vanishes, F_0 is 1, and Fourier inversion yields all expected displacements 1/10. Because phi is irrational, the physical phase flow is dense on the full two-torus for times above any real T. Full support and continuity force the uniform barycenter into the relative interior of the compact phase-image convex hull; relative interiors agree for the convex hull of its dense physical-time tail, giving exact—not only limiting—positive-time attainability. Reflection p_d=p_(10-d) and affine normalization leave dimension at most 5; Caratheodory reduces each representation to <=6 distinct times with positive weights. Independent SymPy exact eigenvalue identification and exact difference census passed; 1369-point direct torus amplitude integration has maximum residual 2.08e-16, and a 1000-candidate numerical late-time linear program found six times >1000 with max residual 2.36e-16. These two numerical tests are corroborative only; symbolic Fourier moments and convex-density argument prove all T and exact equality.

## originality

PASS

Best-of-knowledge PASS: inspected the general arbitrary-law spectral theory, the strongest instantaneous and Cesaro cycle nonmixing theorems, the 2024 survey, the recent arithmetic random-time open-chain classification, and a published P8 exact result. None supplies the exact C10 weighted-torus cancellation or a covering all-cycle existence theorem. General formulas are methods rather than implications. Unindexed harmonic-analysis literature and future reinterpretations remain historical-priority risks.

## value

PASS

The unweighted ten-cycle is a natural first twice-an-odd-prime composite-cycle benchmark beyond C6, with repeated golden-ratio spectrum. Existing sharp nonmixing results concern a single instant or the ordinary Cesaro mean; choosing a common randomized observation time changes the physically meaningful sampling quantifier. This theorem constructs a genuine positive full-support one-harmonic phase law that simultaneously cancels the nontrivial cycle coherences, then derives a rigorous finite support bound for actual times beyond any prescribed cutoff. The exact flat-mixing convex-hull membership of C10 was neither tabulated nor mechanically implied by the inspected source theorems, and the witness gives a natural reusable Fourier cancellation motif. No unproved other-cycle extension or optimality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
