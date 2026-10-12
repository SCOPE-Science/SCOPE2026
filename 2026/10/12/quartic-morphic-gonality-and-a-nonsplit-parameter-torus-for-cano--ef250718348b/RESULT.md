# Quartic morphic gonality and a nonsplit parameter torus for canonical nodal curves

## Finding
Let \(k=\mathbb F_q\) with \(q\) odd, and let \(g\ge4\). Take the canonical Gorenstein nodal curve \(C'\) in [1, Theorem 3.5], with smooth hyperelliptic normalization \(\nu:\widetilde C\to C'\), where \(\widetilde C\) has affine equation \(y^2=f(x)\) with \(f\in k[x]\) squarefree of degree \(2g+1\). The unique node \(Q\in C'(k)\) has a single degree-two normalization point \(P^-\) whose two geometric branches have distinct \(x\)-coordinates \(\alpha,\alpha^q\), for \(\alpha\in k_2\setminus k\) and \(k_2=\mathbb F_{q^2}\), and satisfy \(f(\alpha)\ne0\). Put \(\phi(t)=(t-\alpha)(t-\alpha^q)\in k[t]\).

**Theorem.** The least degree of a finite \(k\)-morphism \(C'\to\mathbb P^1_k\) is \(4\). The set of degree-four such morphisms modulo automorphisms of the target \(\mathbb P^1_k\) is canonically identified, after the displayed choice of the hyperelliptic coordinate, with
\[
T(k)=k_2^\times/k^\times,
\qquad T=(\operatorname{Res}_{k_2/k}\mathbb G_m)/\mathbb G_m.
\]
A class represented by \((a:b)\in\mathbb P^1(k)\) corresponds to the map induced on the normalization by \(R_{a,b}(x)=(a+bx)/\phi(x)\). Thus the number of equivalence classes is exactly \(q+1\). Moreover, \(T\) is precisely the connected affine torus of the generalized Jacobian \(\operatorname{Pic}^0(C')\).

Here *morphic gonality* means the least degree of an everywhere-defined finite morphism onto \(\mathbb P^1_k\); it is deliberately distinguished from the torsion-free-pencil gonality of \([1]\), which is \(3\) for this curve.

## Assumptions and scope
The only permitted curves are the one-node canonical cone curves of [1, Theorem 3.5], not all singular hyperelliptic curves. The base field is the finite field \(k=\mathbb F_q\) of odd characteristic, the normalization genus is at least \(4\), and the closed node branch \(P^-\) has residue field \(k_2\) and is unramified under the hyperelliptic coordinate because \(f(\alpha)\ne0\). The model in [1] identifies the local ring at its sole node as
\[
\mathcal O_{C',Q}=k+\mathfrak m_{\widetilde C,P^-}
\subset\mathcal O_{\widetilde C,P^-}.
\]
All degrees count function-field extension degrees. The parameter classification concerns morphisms over \(k\) modulo **postcomposition** by \(\mathrm{PGL}_2(k)\), with the source curve fixed.

## Proof
**Step 1: low-degree maps must factor through the hyperelliptic coordinate.** Let \(h\in k(\widetilde C)\setminus k\) define a map of degree \(d\le4\) on the normalization. Suppose \(h\notin k(x)\). Because \([k(\widetilde C):k(x)]=2\), the fields \(k(x)\) and \(k(h)\) generate \(k(\widetilde C)\). Hence the joint morphism \((x,h):\widetilde C\to\mathbb P^1\times\mathbb P^1\) is birational onto its integral image \(D\). Its two projection degrees are \(2\) and \(d\), and the arithmetic genus of a curve of this bidegree is \((2-1)(d-1)=d-1\le3\). The genus of its normalization cannot exceed this arithmetic genus, contradicting \(g\ge4\). Thus every function of degree at most \(4\) lies in \(k(x)\). In particular, any nonconstant such \(h\) has even degree and equals \(R(x)\) for a rational map \(R:\mathbb P^1_k\to\mathbb P^1_k\) of degree \(1\) or \(2\).

**Step 2: descent to the node.** A finite map \(C'\to\mathbb P^1\) must send the rational node \(Q\) to a rational target point. By composing with a target automorphism, arrange that its image is \(\infty\). On the normalization, a rational function \(h=R(x)\) has this extension across \(Q\) if and only if \(R(\alpha)=R(\alpha^q)=\infty\), with the equality of the values understood in projective coordinates. Indeed the ring displayed in the assumptions consists precisely of functions regular at the closed point \(P^-\) whose residue is in \(k\); a local target coordinate vanishing at the rational image is then in \(\mathfrak m_{\widetilde C,P^-}\), so the map descends at \(Q\). At every other point, normalization is an isomorphism, and the resulting nonconstant proper morphism is finite.

A degree-one \(R\) cannot send the distinct conjugate points \(\alpha,\alpha^q\) to the same target point, so no degree-two finite morphism exists. Step 1 excludes degrees \(1\) and \(3\), proving the lower bound \(4\).

**Step 3: existence and classification.** Let \(V=H^0(\mathbb P^1,\mathcal O(2))\). A degree-two rational map \(R\) is given by a basepoint-free two-dimensional \(k\)-subspace \(W\subset V\), up to target coordinate change. Its common value at \(\alpha\) and \(\alpha^q\) is rational precisely when some nonzero element of \(W\) vanishes at both points. Such a quadratic section is necessarily a scalar multiple of \(\phi\), so \(\langle\phi\rangle\subset W\). Every such pencil has a unique description \(W=\langle\phi,a+bt\rangle\) with \((a:b)\in\mathbb P^1(k)\), obtained by reducing a second quadratic generator modulo \(\phi\). Because \(\phi\) is irreducible of degree two, \(a+bt\) shares no geometric root with \(\phi\) unless \(a=b=0\); hence every such pencil is basepoint-free. Its induced map has degree \(2\) on \(\mathbb P^1\) and degree \(4\) on \(\widetilde C\). The local function \(\phi/(a+bx)\) vanishes at \(P^-\), giving a finite descended map of degree \(4\) on \(C'\).

**Step 4: the parameter torus and exact count.** Evaluation at \(\alpha\) identifies the two-dimensional quotient \(V/\langle\phi\rangle\) with \(k_2\). The pencil \(\langle\phi,N\rangle\) is basepoint-free exactly when the image of \(N\) is a unit in \(k_2\) (after any field extension, the corresponding unit condition applies in the tensor algebra). Thus the open pencil parameter functor is the torus \(T=(\operatorname{Res}_{k_2/k}\mathbb G_m)/\mathbb G_m\). On \(k\)-points, \(T(k)=k_2^\times/k^\times\), whose order is \((q^2-1)/(q-1)=q+1\). No two distinct pencils yield target-equivalent maps because postcomposition changes a basis of \(W\) but not \(W\) itself.

**Step 5: generalized Jacobian identification.** The normalization exact sequence for the nonsplit node identifies the local multiplicative descent obstruction with \(\operatorname{Res}_{k_2/k}\mathbb G_m/\mathbb G_m\), and gives a semiabelian extension
\[
1\longrightarrow T\longrightarrow\operatorname{Pic}^0(C')
\longrightarrow\operatorname{Jac}(\widetilde C)\longrightarrow1.
\]
This identifies the parameter torus with the affine torus of the generalized Jacobian; it does not claim that the extension splits.

## Verification
The separate standalone script `verify.py` performs exact finite-field arithmetic for \(q\in\{3,5,7,11,13,17\}\), computes the \(q+1\) projective classes in the quadratic extension, verifies closure under multiplication, and tests an explicit genus-four source in characteristic three. It returns `VERIFY_OK`. These computations check examples, not the universal quantifiers: the general proof is Steps 1–5.

An explicit nonempty example is \(k=\mathbb F_3\), \(g=4\), \(f(t)=t^9-t+1\), \(\phi(t)=t^2+1\). Here \(f'=-1\), so the normalization is smooth, \(\phi\) is irreducible, and for its root \(\alpha\in\mathbb F_9\) one has \(f(\alpha)=1\). The four target-equivalence classes are represented by \((a:b)\in\mathbb P^1(\mathbb F_3)\).

## Relationship to prior work
Hilario, Salomão and Martins [1, §§3.4 and 4] construct the canonical nodal curves, identify their normalization rings and prove their torsion-free-pencil gonality is \(3\). Their article explicitly distinguishes generalized linear-series gonality from covers to \(\mathbb P^1\), and does not give this exact finite-morphism classification or \(q+1\) enumeration. Rosa and Stöhr [2] develop the ambient theory of trigonal Gorenstein curves and their nonremovable base points; an equivalent earlier formula in their full paper cannot be excluded without a complete reading. Faber, Grantham and Howe [3] study morphic gonality of smooth curves, not this nodal source and its split/nonsplit descent condition. The genus bound used in Step 1 is a standard bidegree-genus inequality; novelty is not claimed for that principle alone.

## Limitations
The result applies only to the specified one-nonsplit-node models, odd characteristic and normalization genus at least four. It does not classify degree-five or higher covers, covers of other singular curves, automorphisms of the source, genus-three boundary cases, or the extension class of the generalized Jacobian. The older Rosa–Stöhr article [2] was only partly accessible during source comparison; it could contain an implicit equivalent classification. Verification tests do not constitute an exhaustive census over all finite fields.

## References
[1] C. Hilario, R. Salomão and R. V. Martins, *Maximal singular curves over finite fields from elliptic and hyperelliptic curves*, arXiv:2609.22557, first posted 2026-09-18, version 2 dated 2026-09-22, especially Theorems 3.5 and 4.8 and §§3.4,4; https://arxiv.org/pdf/2609.22557.

[2] R. Rosa and K.-O. Stöhr, *Trigonal Gorenstein curves*, Journal of Pure and Applied Algebra 174 (2002), 187–205, https://doi.org/10.1016/S0022-4049(02)00122-6.

[3] X. Faber, J. Grantham and E. W. Howe, *On the maximum gonality of a curve over a finite field*, Algebra & Number Theory 19 (2025), arXiv:2207.14307; https://arxiv.org/abs/2207.14307.
