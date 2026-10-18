# One propositional variable already destroys local finiteness in Alexandrov dynamic topological logic

## Finding

In the Boolean dynamic topological language with spatial interior/closure, deterministic temporal next and future eventuality, one propositional variable suffices for a satisfiable formula with **no model whose distinguished point generates a finite spatial upset**. The variable-free fragment has a one-point model for every satisfiable formula. Hence the sharp minimum number of propositional variables witnessing failure of the locally finite model property is **one**. All models here are Alexandrov spaces, equivalently preorders with a monotone temporal self-map. This conclusion is for full dynamic topological logic, not its restricted fragments.

## Assumptions and scope

A dynamic preorder model is a quadruple \((W,\preceq,f,V)\), where \(W\ne\varnothing\), \(\preceq\) is reflexive and transitive, \(f:W\to W\) is order preserving, and \(V\) assigns arbitrary subsets of \(W\) to propositional variables. Boolean connectives are evaluated classically. Define \(w\models\Diamond\alpha\) iff some \(u\succeq w\) satisfies \(\alpha\), \(w\models\bullet\alpha\) iff \(f(w)\models\alpha\), and \(w\models F\alpha\) iff \(f^n(w)\models\alpha\) for some integer \(n\ge0\). Write \(\Box\alpha:=\neg\Diamond\neg\alpha\) and \(G\alpha:=\neg F\neg\alpha\). The generated upset of \(w\) is \(\uparrow w=\{u:w\preceq u\}\).

Using a single atom \(r\), define
\[
D(r):=(r\wedge\neg\bullet r)\vee(\neg r\wedge\bullet r),\qquad
Q(r):=\neg F D(r),\qquad
P(r):=(r\wedge\neg Q(r))\vee(\neg r\wedge Q(r)).
\]
Thus \(D\) detects a temporal truth-value change, \(Q\) says no change occurs now or later, and \(P\) is the Boolean exclusive-or of \(r\) and \(Q\). For formulae \(a,b\), put
\[
\begin{aligned}
\psi_1(a,b)&:=G\Box\big((a\to\bullet a)\wedge(\neg a\to\bullet\neg a)\wedge(b\to\bullet b)\big),\\
\psi_2(a,b)&:=\Box\big((a\to\Diamond\neg a)\wedge(\neg a\to\Diamond a)\big),\\
\psi_3(a,b)&:=\Box\big(a\to F(b\wedge\neg\Diamond(\neg a\wedge b))\big),\\
\psi_4(a,b)&:=\Box\big(\neg a\to F(b\wedge\neg\Diamond(a\wedge b))\big).
\end{aligned}
\]
The single-variable formula in the theorem is \(\Psi(r):=\bigwedge_{i=1}^{4}\psi_i(P(r),Q(r))\), where each occurrence is ordinary literal substitution into the displayed formula schemata. No additional propositional atom, constant naming a world, hybrid binder, or quantifier is used.

## Proof

**1. An infinite satisfying model and one-variable decoding.** Take \(W=\mathbb N_0\times\mathbb N_0\). Order only within fixed time slices: \((i,j)\preceq(k,l)\) precisely when \(j=l\) and \(i\le k\). Put \(f(i,j)=(i,j+1)\), an order-preserving total map. Define the auxiliary Boolean observations \(p(i,j)\) to mean that \(i\) is even and \(q(i,j)\) to mean \(j\ge i\). Finally set the *only actual atomic valuation* \(r(i,j):=p(i,j)\oplus q(i,j)\).

For every \(i\ge1\), along the temporal orbit of \((i,j)\), the truth of \(r\) flips exactly once, between temporal indices \(i-1\) and \(i\); for \(i=0\), it never flips. Consequently \(\neg F D(r)\) holds at \((i,j)\) exactly when \(j\ge i\), so \(Q(r)=q\) pointwise, and then \(P(r)=r\oplus Q(r)=p\). It is therefore enough to check the four schemata on \(p,q\).

The truth of \(p\) never changes under \(f\), while \(q\) is persistent toward the future; this proves \(\psi_1\). Every \((i,j)\) has a spatial successor \((i+1,j)\) of the opposite parity, proving \(\psi_2\). For each spatial successor \((i,0)\) of the distinguished point \((0,0)\), move temporally to \((i,i)\). There \(q\) holds, but at every proper spatial successor \((k,i)\) with \(k>i\), \(q\) fails. Thus no opposite-parity point carrying \(q\) is spatially accessible at that time. This simultaneously proves \(\psi_3\) and \(\psi_4\) at \((0,0)\). Hence \(\Psi(r)\) is satisfiable.

**2. No finite generated upset.** This step works for *arbitrary* formulae \(a,b\) interpreted as two Boolean observations, not merely atomic variables. Suppose \(w\models\bigwedge_i\psi_i(a,b)\), and suppose \(\uparrow w\) is finite. From \(\psi_2\) construct an infinite spatially nondecreasing chain of worlds \(w=w_0\preceq w_1\preceq w_2\preceq\cdots\), with successive points satisfying opposite truth values of \(a\). Since \(\uparrow w\) is finite, some \(w_s=w_t\) for \(s<t\), and then \(w_s\preceq w_{s+1}\preceq w_t=w_s\). Hence there are mutually accessible points \(x,y\succeq w\) with \(x\models a\), \(y\models\neg a\).

Write \(x_m=f^m(x)\) and \(y_n=f^n(y)\). By \(\psi_3\) at \(x\), choose \(m\ge0\) such that \(x_m\models b\wedge\neg\Diamond(\neg a\wedge b)\). By \(\psi_4\) at \(y\), choose \(n\ge0\) such that \(y_n\models b\wedge\neg\Diamond(a\wedge b)\). The global temporal-spatial condition \(\psi_1\) guarantees that \(a\) keeps its initial, opposite values along both temporal orbits and that once \(b\) is true it persists under further temporal iterations. Monotonicity of \(f\) preserves the mutual accessibility of the two orbits at equal indices.

If \(m\le n\), then \(x_n\models a\wedge b\) and \(y_n\preceq x_n\), contradicting the condition at \(y_n\). If \(n\le m\), then \(y_m\models\neg a\wedge b\) and \(x_m\preceq y_m\), contradicting the condition at \(x_m\). The two alternatives exhaust all possibilities, so \(\uparrow w\) cannot be finite. Substituting \(a=P(r)\), \(b=Q(r)\) preserves this argument, proving the obstruction for \(\Psi(r)\).

**3. Sharpness.** In a variable-free Boolean formula (allowing the usual truth and falsity constants), every subformula is either true at all worlds or false at all worlds, by induction: the spatial operators respect \(\varnothing\) and \(W\) because the order is reflexive, and deterministic next and future eventuality also respect them. Therefore a satisfiable variable-free formula is true at the unique world of the singleton reflexive model with its identity temporal map. A zero-variable obstruction is impossible. This proves sharp one-variable minimality.

## Verification

Run `python CHECK.py` using Python 3 standard library. The checker verifies the temporal-change encoding on a \(32\times32\) grid and the four source-obstruction obligations on a \(24\times24\) finite window. It independently enumerates all preorders with one, two or three labeled worlds, all monotone temporal maps and all unary valuations and evaluates the exact expanded formula directly. Expected output is `ONE_ATOM_DTL_VERIFY_OK decoding=1024 grid_obligations=576 preorders=34 monotone_maps=390 finite_models=3058`. The finite tests do **not** prove the universal nonexistence assertion; the proof above does.

## Relationship to prior work

Vooijs and Fernández-Duque (2026), Lemma 3.1, give the underlying four-condition obstruction to a finite generated upset using *two independent propositional variables*. The present claim sharpens the minimum number of genuine atoms by encoding the two observations into one temporal-change signal and proves that zero atoms cannot work. This is not a claim that the two-variable obstruction is new. Konev, Kontchakov, Wolter and Zakharyaschev (2006) establish local finiteness for their restricted \(\mathrm{DTL}_1\) language and contrast it with full dynamic topological logic; their restriction does not include the needed nesting of future eventuality inside spatial operators. Neither inspected primary source states the one-variable sharpness claim.

## Limitations

The result concerns Alexandrov/preorder semantics with deterministic monotone temporal maps, not arbitrary non-Alexandrov topological spaces or relational/non-deterministic temporal transitions. It is an existence and sharp-variable theorem, not a satisfiability-complexity bound. The 2006 and 2026 relevant primary statements were inspected; an older or differently named unary-variable construction could imply the same result, so absolute historical priority is not claimed. Computational checks are finite corroboration only.

## References

1. Niels C. Vooijs and David Fernández-Duque, *Axiomatizability of Alexandrov Dynamic Topological Logic*, LICS 2026, Article 81, especially §3, Lemma 3.1. DOI `10.4230/LIPIcs.LICS.2026.81`. Public source date 2026-07-09. Open-access full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol380-lics2026/LIPIcs.LICS.2026.81/LIPIcs.LICS.2026.81.pdf.
2. Boris Konev, Roman Kontchakov, Frank Wolter and Michael Zakharyaschev, *Dynamic topological logics over spaces with continuous functions*, Advances in Modal Logic 2006, especially §§2–3, Lemmas 5–6. Open-access full text: https://cgi.csc.liv.ac.uk/~frank/publ/dyntopo-aiml.pdf.
