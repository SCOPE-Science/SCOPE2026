# Independent mathematical audit

## correctness

PASS

Re-audited the nonbinary theorem in /workspace/repairs/2/RESULT.md. The spectral bright space is the orthogonal sum of the spans of the two projected absorbers at each eigenvalue. Its complement is a direct sum of annihilated eigenspace components, not necessarily composed of individual adjacency eigenvectors as the frozen proof wording could suggest. The two spaces reduce adjacency and loss. On the bright space, taking the inner product of an effective eigenvector with its eigenvalue equation rules out zero imaginary part by positivity and the definition of the complement; all its Jordan components decay. This proves U†U tends to the dark projector and gives the exact trace identity even for coherent density matrices. The tensor projectors C=J/q and D=I−J/q furnish the q-ary Krawtchouk kernel with normalization q⁻ᵈ. At every nonconstant level k, K_k(h)/B_k is the mean of (−1/(q−1))^J for the number J of differing positions in a uniform k-subset. Because h≥1 and q≥3, J>0 has positive probability and those summands have modulus below one, proving strict rank two even at k=d and for composite q. The constant level contributes one dimension and q⁻ᵈ to the site law. Gram inversion gives the sitewise formula; tracing recovers the uniform mean, and removing the two certain-absorption vertices gives the conditional mean. For d=1 the nonsink probability is 1/(q−2); q=3,d=1 is full absorption. Independently evaluated the H(2,3) example with exact fractions, giving 3/5 and 2/5 with unchanged average 5/9. The frozen binary formula is also mathematically sound: for h=d all k-subsets give the same sign, while for 1≤h<d interior k allow both signs; its adjacent case splits off the first coordinate, and d=1 is two fully absorbing vertices. The submitted numerical checker was inspected, not executed; its finite scope is reported in the repair.

## originality

PASS

The frozen originality claim FAILS as written: its two-absorber binary ranks, antipodal redundancy and binary sitewise law were already explicitly published in Resultary e6d55236b096, dated October 12. The d=1 endpoint and adjacent-binomial simplification do not rescue novelty for that branch. The revised result removes the binary branch from the Finding, explicitly credits it, and re-audits the nonbinary rank and sitewise law already contained in the October 27 evidence. The closest same-family and stronger distance-regular absorption records located for that retained claim are dated November 2, and are acknowledged as mathematical coverage, not preemption of the October 27 nonbinary finding. No novelty is claimed for the abstract spectral-projection method or for the boundary check d=1 in isolation.

## value

PASS

The nonbinary theorem independently solves the two-site placement question on a natural infinite family, including composite alphabets. Every nonconstant spectral block has two independent capture directions, explaining why placement cannot change the overall average, unlike the prior binary obstruction. The explicit site law also separates placement invariance of the mean from placement sensitivity of local capture, as the exact H(2,3) example shows. This is not novelty assigned to the old binary ranks, their small edge cases or a generic rewriting of Gram inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
