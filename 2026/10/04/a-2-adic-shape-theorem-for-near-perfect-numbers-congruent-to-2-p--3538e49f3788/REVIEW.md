# Same-model review

## Correctness
PASS. From \(\sigma(2m)=3\sigma(m)=4m+d\), parity gives \(d\) odd exactly when \(\sigma(m)\) is odd, which for odd \(m\) is exactly the square condition. In the nonsquare case \(d\mid2m\) forces \(v_2(d)=1\); after division by two, parity forces \(v_2(\sigma(m))=1\). Multiplicativity then permits exactly one odd prime exponent, and the 2-adic lifting identity \(v_2(\sigma(p^a))=v_2(p+1)+v_2(a+1)-1\) for odd \(p,a\) forces both \(p\equiv1\pmod4\) and \(a\equiv1\pmod4\). No finite search is used for the infinite step.

## Originality
PASS. Pollack--Shevelev give construction families and the odd-redundant-divisor conjecture; Ren--Chen classify the two-distinct-prime-factor case; Tang--Ma--Feng concern odd near-perfect integers. Full-text inspection of the most relevant archive sources found no arbitrary-support theorem for the slice \(v_2(n)=1\), no equivalence between odd redundant divisor and square odd part there, and no \(p^{4u+1}s^2\) alternative. OEIS A181595 supplies examples rather than an implication theorem. Search risk remains because elementary observations can be stated without standard terminology, but no stronger or equivalent statement was located.

## Value
PASS. The result turns one congruence slice of the open even near-perfect classification problem into a rigid exponent-parity dichotomy valid at arbitrary prime support. It explains why the first examples \(18,234,650\) have their observed odd-part shapes and links the classical odd-redundant-divisor question to a square condition. This is a reusable structural filter, not a bounded census or a parameter renaming.

## Closest literature and limitations
The closest implication-level source is Ren--Chen's complete \(\omega(n)=2\) classification, which is narrower in prime support. Pollack--Shevelev's odd-redundant-divisor conjecture overlaps one consequence but does not imply the odd-part square criterion. The theorem is necessary only and does not classify the admissible shapes.

Same-model review: passed. Independent audit: not yet performed.
