# Independent mathematical audit

## correctness

PASS

The trace is onto (its defining polynomial has degree q³<q⁴ and is nonzero), so ker τ has size q³. For z=x+x^q one has z+z^(q²)=τ(x) and τ(G_q(x))=τ(x)(1+τ(z^(q−1))). This proves the zero-input-trace case. For nonzero w, z=wy reduces to y^(q²)+y=1 and τ(y^(q−1))=1, with exactly q lifts per qualifying y by the image and kernel of x↦x+x^q. With t=y+y^q, v=y²+y, h=t²+t, we have t^q=t+1 and v^q=v+h, so h has absolute trace one. The tower trace gives τ(y^(q−1))=t/v+(t+1)/(v+h), where the denominators are nonzero. Writing b=v+th yields b²+(h+1)b+h³=0. For h≠1 the Artin–Schreier right side h³/(h+1)²=h+(h+1)^−1+(h+1)^−2 still has trace one, impossible. For h=1, b=1, s is odd and y²+y=t+1 with t²+t=1; thus y⁴+y=1 and y⁸+y=t. The four distinct roots from the two t's lie in F16⊂F_(q^4), and satisfy the required q-Frobenius exactly for s≡3 mod 4. Hence the total fiber exceeds q³ exactly in that class, excluding permutations there but making no other permutation assertion. `python3 /workspace/branches/independent_checks.py 3` verifies field irreducibility and enumerates G_q in alternate polynomial bases for q=4,8,16, giving totals 64,736,4096 and checking every input trace class. This is bounded corroboration; the uploaded checker was inspected, not executed.

## originality

PASS

The e=4 polynomial is explicitly an antecedent and its q=4 permutation instance is already in the prior desirable-triple table. The supported increment is the uniform classification of the joint fibers and the resulting infinite nonpermutation class s≡3 mod 4, not the polynomial, use of trace maps, or the isolated q=4 case. No inspected earlier statement or implication gives that uniform classification.

## value

PASS

The zero output trace is a natural permutation test because its target size is exactly q³. The result quantifies the full excess split by input trace and explains it by four uniform F16 witnesses rather than a finite counterexample. It answers a meaningful part of the exact e=4 parameter question for an infinite class and can guide further analysis of the balanced classes. It is not the full classification of Question 6.1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
