# Independent mathematical audit

## correctness

PASS

Independently recomputed the exact rational composition g=f∘f and identities f(x)-1=-(x-1)(6x+5)/(8x²+3), g(x)-x=-56(x-1)^3(4x²+3x+4)/Q(x), and g(x)-1=(x-1)(6x+5)(52x²+6x+63)/Q(x), Q=224x⁴+32x³+408x²+128x+539. Every factor Q and each multiplier is positive on x>0; g preserves the side of 1 and moves strictly toward it, ruling out other positive limits. Independent SymPy recomposition gives g(1+u)-1=u-56u³/121+280u⁴/1331+224u⁵/1331-3136u⁶/14641+O(u⁷); inverse-square increment is A+Bu+C₂u²+O(u³), A=112/121, B=-560/1331, C₂=4480/14641. With σ fixed and w_n=(x_{2n}-1)^(-2), Δw=A+σB w^-1/2+C₂w^-1+O(w^-3/2), yielding w=An+O(√n), then w=An+σp√n+O(log n), p=2B/√A=-40√7/121; substitution yields q=C₂/A-B²/A²=15/121. After subtracting An+σp√n+qlog n, increments are O((1+log n)n^-3/2), absolutely summable. Verifies existence of a finite C(x₀) for all x₀>0, x₀≠1 in unmodified 2n physical iterations. Independent 50-digit 5000-pair examples for x₀=0.3 and 2 corroborate the correction but are not the infinite proof.

## originality

PASS

BEST-OF-KNOWLEDGE and qualified: the 2022/2023 original establishes the exact map and τ=2 flip, not the orbit-specific signed √n and log expansion with global finite constant; the 2026 critical-slowing paper truncates at cubic order, giving only the known exponent and leading behavior. General parabolic Fatou-coordinate theory supplies a method/expansion existence but was not found to state or directly evaluate the rational-map coefficients in the original physical coordinate. Resultary exact-match returns this same finding (not independent support); no different source located with an implication that evaluates this exact claim. Priority remains uncertain because routine specialization of general parabolic theory or an unindexed computation may already contain it.

## value

PASS

The τ=2 flip is a natural threshold of a published positivity-preserving numerical discretization. Critical slowing is a mathematically motivated phenomenon, and exact leading power law alone does not distinguish approaches from above/below or quantify finite-time bias. The signed √n correction, universal 15/121 logarithmic correction, and finite renormalized remainder for every positive initial state give a precise, independently useful model-specific relaxation benchmark. Their exact values require the nontrivial higher jet and summable-error argument; they are not a mere parameter rename, trivial type check or tabulated recomputation. No general multi-parameter theorem or new universal exponent is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
