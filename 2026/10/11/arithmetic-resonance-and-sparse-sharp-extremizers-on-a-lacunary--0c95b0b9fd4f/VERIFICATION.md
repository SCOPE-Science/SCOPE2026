---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For any nontrivial additive character, summing fourth powers over F_q^3 with probability output gives the exact ordered-pair energy Q=Σ_{γ(a)+γ(b)=γ(c)+γ(d)}f(a)f(b)conj(f(c)f(d)), with no q prefactor. In characteristic >=5, set s=a+b. When s≠0, a^3+b^3=s^3−3sab recovers ab and therefore the unordered pair; no nontrivial collisions remain. When s=0, pairs are (a,−a) with fourth-coordinate sum 2a^4. Since F_q^× is cyclic, fourth roots are exactly ±1 when q≡3(mod4) and ±1,±i when q≡1(mod4). In the first case Q=2S²−Σ_t|f(t)|⁴≤(2−1/q)S², with equality for every and only constant positive magnitude on all q points; any phases. In the second, distinct nonzero fourth-root orbits are disjoint four-point sets O; the exact correction is +8Σ_O Re[f(a)f(−a) overline(f(ia)f(−ia))]. Let α=|f(0)|²,w_O=Σ_{t∈O}|f(t)|². By AM–GM and Cauchy each orbit's net correction to −Σ|f|⁴ is ≤w_O²/4, with equality only at four equal magnitudes and aligned opposite-pair products. Thus Q≤2S²−α²+(1/4)Σw_O²≤2S²−α²+(S−α)²/4≤(9/4)S². For S>0 equality forces α=0, exactly one orbit of positive mass, equal four magnitudes, U=V; conversely each such f attains 9/4. Hence exact operator norm fourth powers and the complete complex phase classification hold for every prime-power q of characteristic >3. Independently rebuilt additive pair-sum fibers and fourth-moment energies for p=5,7,11,13,17,19,23 and F25/F49, with 4 seeded Gaussian-integer complex vectors per field plus equality witnesses: every fiber was single or exactly a 2-pair zero-sum fiber, and counts were 1,0,0,3,4,0,0,6,12 in the listed order. These finite tests corroborate, not prove, the all-q algebraic claim. Canonical Git tree SHA independently reproduced.

## originality

PASS

Best-of-knowledge originality of the full all-characteristic>=5, all-prime-power two-regime sharp L²→L⁴ constant and complete extremizer classification for γ(t)=(t,t³,t⁴) is supported, but foundational tools and some slices are prior. Direct inspection of Mockenhaupt–Tao, Koh–Shen, Biswas et al. (Sections 1,2,3.3), Lewko–Lewko, and three published Resultary research results revealed no theorem implying all field sizes and the complete mod-four phase/support dichotomy. General additive-energy orthogonality, Sidon flat extremizers, and a single parallelogram defect's 9/4 extremizer are established/independently published mechanics, not claimed new. A published same-date one-defect result implies q=5 as a special case; it explicitly assumes only one double pair-sum fiber, whereas current q=13,17,25,... has 3,4,6,... disjoint nontrivial fibers, and it does not classify the curve/field progression. The published q≡3 branch is a standard Sidon equality case. The submitted new combination is the polynomial fiber classification and exact global sparsity/equality geometry across arbitrary extension fields. The close Resultary identical record is the assigned finding and is excluded as independent prior priority. Priority conclusions remain qualified: generalized Λ(4) or additive-energy results could imply the disjoint-fiber estimate, and same-day priority between independent records was not established.

## value

PASS

The curve γ(t)=(t,t³,t⁴) is a simple natural lacunary polynomial moment curve. Unlike consecutive-monomial moment curves, removing the quadratic coordinate leaves arithmetic fourth-root collision classes, a genuine structural feature. The theorem determines a sharp normalized Fourier extension invariant for every finite field in characteristic>=5 and classifies all complex extremizers, with a sharp transition between flat full support (q≡3 mod4) and sparse four-point support plus a nontrivial product-phase constraint (q≡1 mod4). These exact equality and norm facts could be used to compare restriction/equality mechanisms and concentration under added/missing coordinates. Though its optimization uses elementary inequalities once the pair fibers are found, identifying the complete arithmetic fibers and global optimizer geometry is a motivated infinite-family exact classification, not a mere numerical table or arbitrary slice. No more general Lacunary curve theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
