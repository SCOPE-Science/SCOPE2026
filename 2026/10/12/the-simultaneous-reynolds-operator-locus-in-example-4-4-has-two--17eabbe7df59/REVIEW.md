# Independent mathematical audit

## correctness

PASS

Independent basis-pair/triple derivation, without relying on the recorded Gröbner basis: write R=[[a,b,c],[d,e,f],[g,h,i]] and v=(b,e,h). The Lie equations are Δ_ij e2=(L_ij−Δ_ij)v, with Δ=(ae−bd,af−cd,bf−ce) and L=(a+e,f,−c). If v=0 these leave af−cd=0 and the ternary equation is automatic. If v and e2 are independent they give Δ=L=0, exactly the X2 conditions; det R and the sum of its principal 2×2 minors then both vanish, giving the ternary identity. In the remaining case v=e e2, e≠0, the Lie equations give a=1, c=f=0. The ternary equation is det(R)e2=(sum of principal 2×2 minors−det R)v; here it reads ei=e(e+i), impossible. This proves necessity and sufficiency. The determinant and rank-three quadratic factors are irreducible, giving dimensions 5 and 5; adding the component ideals gives the stated A³ intersection. E13 and E21+E32 satisfy the undivided conditions and lie outside both printed charts. RESULT.md and artifacts/verify.py were inspected, not executed. This is a set-theoretic statement, not a claim of a reduced raw defect scheme.

## originality

PASS

Pass the completed set-theoretic component and boundary description, not the Reynolds identities or the undivided equations. Hou–Sheng already provide necessary-and-sufficient undivided equations via Theorem 4.2, and their example splits into cases, but the divisions in the displayed terminal parametrizations do not resolve the zero-denominator cases. The source calls the two displays operators; it does not explicitly state that those displays alone are an exhaustive iff.

## value

PASS

This corrects a concrete zero-denominator omission in a named example: the lost operators are positive-dimensional boundary loci needed to use it as a classification. The closed components and their overlap also describe how the two families fit together. The useful result is the completed example, not re-deriving its defining equations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
