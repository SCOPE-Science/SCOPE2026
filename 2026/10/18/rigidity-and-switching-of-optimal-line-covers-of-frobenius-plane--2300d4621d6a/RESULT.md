# Rigidity and switching of optimal line covers of Frobenius plane curves

## Finding

For each prime power \(t\ge3\) and \(h\ge2\), set \(q=t^h\). Let \(C_t\) be the projective plane curve
\[
C_t:\quad YZ^{t-1}=X^t\quad\text{over}\quad\mathbf F_q.
\]
Its exact rational-point covering number by distinct \(\mathbf F_q\)-lines is \(q/t+1\). Every optimal cover uses precisely one line through \(P_\infty=[0:1:0]\); its other \(q/t\) lines are maximal \(t\)-secants. If \(h=2\), the secants necessarily form one affine parallel class, and the complete number of optimal covers is
\[
(t+1)(t^2+1).
\]
If \(h\ge3\), optimal covers exist with two distinct secant directions. The quadratic-extension rigidity therefore disappears at extension degree three.

## Assumptions and scope

The characteristic is arbitrary. The parameter \(t\) is a prime power at least three (not necessarily prime), \(h\) is an integer at least two, and \(q=t^h\). Count unordered sets of distinct projective lines defined over \(\mathbf F_q\), not ordered presentations. All assertions concern \(\mathbf F_q\)-rational points, not geometric points. The curve is geometrically integral: the defining polynomial is primitive and linear in \(Y\), with coprime coefficients \(Z^{t-1}\) and \(X^t\).

## Proof

**Step 1: Incidences.** The curve has the \(q+1\) rational points \(P_s=[s:s^t:1]\) for \(s\in\mathbf F_q\), together with \(P_\infty=[0:1:0]\). A projective line through \(P_\infty\) has an affine equation \(X=cZ\), or is \(Z=0\); thus it has at most one affine curve point. Every other line is uniquely \(Y=mX+cZ\). Its intersections solve \(s^t-ms=c\). The additive map \(s\mapsto s^t-ms\) is \(\mathbf F_t\)-linear. If its kernel has a nonzero element \(u\), then \(s^t=ms\) holds precisely for \(s\in\mathbf F_t u\), since \((s/u)^t=s/u\) characterizes \(\mathbf F_t\). Therefore a nonempty line section has either one or \(t\) rational affine points (an empty section is also possible). Its \(t\)-point sections are precisely the cosets \(s_0+\mathbf F_tu\), with \(u\ne0\); each has its uniquely determined projective secant \(Y=u^{t-1}X+(s_0^t-u^{t-1}s_0)Z\). Thus maximal secants correspond bijectively to affine one-dimensional \(\mathbf F_t\)-subspaces of the additive space \(\mathbf F_q\).

**Step 2: Optimal cardinality and forced secants.** Since any line contains at most \(t\) rational curve points, \(q+1\) points need at least \(\lceil(q+1)/t\rceil=q/t+1\) lines. Conversely, the \(q/t\) cosets of a fixed \(\mathbf F_tu\) partition the affine points, and adjoining the line \(Z=0\) covers \(P_\infty\). So the lower bound is attained. Put \(a=q/t+1\). In a cover of size \(a\), let \(v\) lines pass through \(P_\infty\). Necessarily \(v\ge1\). The number of affine points covered is at most \((a-v)t+v\). If \(v\ge2\), this is at most \(q-t+2<q\), a contradiction. Thus \(v=1\). If any of the remaining \(q/t\) lines has fewer than \(t\) affine points, it contributes at most one; even allowing one affine point on the line through infinity, the total is at most \(q-t+2<q\). Hence every remaining line is a \(t\)-secant. Their \(q\) incidences can cover all but at most one of the \(q\) affine curve points.

**Step 3: Quadratic-extension rigidity.** For \(h=2\), view \(\mathbf F_q\) as the affine plane \(\operatorname{AG}(2,t)\). There are \(t\) maximal secants in an optimal cover. Suppose two source affine lines have different directions; they intersect at one point, so their union has \(2t-1\) points. Each additional affine line of the plane meets their union (if parallel to the first, it meets the second; otherwise it meets the first), so it adds at most \(t-1\) new points. Therefore all \(t\) secants together cover at most \(2t-1+(t-2)(t-1)=t^2-t+1\) affine points; the line through infinity adds at most one more. Since \(t\ge3\), \(t^2-t+2<t^2\), contradiction. Thus all \(t\) maximal secants are disjoint and share a direction, forming a complete parallel class. The plane has exactly \(t+1\) parallel classes. There are exactly \(q+1=t^2+1\) projective lines through \(P_\infty\), independently selectable; no duplications occur. The total is \((t+1)(t^2+1)\).

**Step 4: Higher-extension switching.** For \(h\ge3\), choose independent vectors \(u,v\) in \(\mathbf F_q\) over \(\mathbf F_t\), and let \(A=\mathbf F_tu+\mathbf F_tv\). Begin with all \(q/t\) cosets of \(\mathbf F_tu\), a partition of \(\mathbf F_q\). Exactly \(t\) of these lie in \(A\), and every other coset is disjoint from \(A\). Replace those \(t\) cosets by the \(t\) cosets of \(\mathbf F_tv\) inside \(A\). The new \(q/t\) affine \(\mathbf F_t\)-lines still partition \(\mathbf F_q\) and use both directions. Their corresponding maximal secants, together with any line through \(P_\infty\), form a nonparallel optimal cover.

## Verification

Execute `python3 check.py` using the Python standard library. It enumerates all \(91\) projective lines over \(\mathbf F_9\), checks every four-line subset, and finds exactly \(40\) optimal covers. For \(\mathbf F_{27}\) it checks a plane switch and the distinct secant directions. These finite calculations check examples only; the preceding argument proves every allowed prime power and exponent.

## Relationship to prior work

Asgarli et al., arXiv:2610.13042v1, formulate the exact line-cover problem and prove a covering-number formula for the different nonreflexive family of degree \(p^2\) over odd-degree extensions of \(\mathbf F_p\). Their Proposition 4.1 does not classify all optimal covers, and it does not give the quadratic-extension enumeration and extension-degree switching theorem here. The affine-line counting and parallel-class facts themselves are standard finite geometry; the contribution concerns the optimal covers of this specific geometrically integral curve family, rather than a new theorem about abstract affine planes.

## Limitations

No classification or enumeration of all optimal covers for \(h\ge3\) is claimed. The statement also excludes \(t=2\), where the counting obstruction for one uncovered affine point changes. Search results cannot exclude an equivalent older computation that is not indexed. The result is a self-reviewed finding, not an independently audited theorem.

## References

1. Asgarli, Dassarma, Ghioca, MacLean, and Stokdyk, Covering plane curves over finite fields with lines (2026), arXiv:2610.13042v1, Introduction and Proposition 4.1. https://arxiv.org/html/2610.13042v1
2. Finite affine-plane axioms and parallel classes, Mathematics LibreTexts, Affine Planes. https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Combinatorics_(Morris)/04%3A_Design_Theory/18%3A_More_Designs/18.03%3A_Affine_Planes
