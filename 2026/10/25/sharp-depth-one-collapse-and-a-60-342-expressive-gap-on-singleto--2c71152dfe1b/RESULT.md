# Sharp depth-one collapse and a \(60:342\) expressive gap on singleton fuzzy Gödel frames

## Finding

Let \(\mathcal F_1\) be the class of all one-world fuzzy Gödel Kripke models with one propositional letter \(p\), a single accessibility weight \(r\in[0,1]\), and an arbitrary valuation \(x=e(w,p)\in[0,1]\). Formulas use \(\bot,\wedge,\vee,\to\), with \(\top:=\bot\to\bot\), and either only \(\Box\), only \(\Diamond\), or both modalities. Identify formulas when they have the *same truth degree* for every \((r,x)\in[0,1]^2\), not merely the same designated-truth set.

The purely propositional one-letter fragment has exactly \(6\) semantic classes. On \(\mathcal F_1\), the \(\Box\)-only fragment has **exactly \(60\)** classes, whereas the \(\Diamond\)-only and full bimodal fragments both have **exactly \(342\)** classes. Every formula in any of these modal fragments is equivalent on \(\mathcal F_1\) to a formula of modal nesting depth **at most one**; this bound is sharp for each modal fragment. In particular, the \(\Box\)-only language is strictly weaker than the \(\Diamond\)-only language even on the smallest possible fuzzy frame, although \(\Diamond\) alone defines \(\Box\) on this class:
\[
\Box\varphi\equiv(\Diamond\top\to\varphi).
\]

The number \(342\) is the previously known size of the free two-generated Gödel algebra, not itself a novelty claim. The specific \(60\)-element \(\Box\)-fragment and the joint sharp depth-one classification are the focus.

## Assumptions and scope

The Gödel operations are \(a\wedge b=\min(a,b)\), \(a\vee b=\max(a,b)\), and \(a\to b=1\) if \(a\le b\), otherwise \(b\). On the only world \(w\), the modalities reduce to
\[
 e(w,\Box\varphi)=r\to e(w,\varphi),\qquad
 e(w,\Diamond\varphi)=\min(r,e(w,\varphi)).
\]
These are automatically witnessed semantics. **No reflexivity constraint \(r=1\) is imposed**; imposing crisp, reflexive, or fixed numerical access weights changes the statement. Propositional valuations and accessibility weights range over the entire real unit interval, and no intermediate truth constants are named in the language.

Modal nesting depth counts only nested \(\Box\) or \(\Diamond\) operators. Gödel propositional connectives may be arbitrarily nested. Equivalence is equality of real-valued term functions on every singleton frame and every valuation, rather than validity equivalence over all Kripke frames.

## Proof

**Step 1: Reduction to finitely many ordered cases.** By structural induction, every formula value at the sole world is one of \(0,1,r,x\): the propositional operators select an input or an endpoint, while \(r\to\cdot\) and \(\min(r,\cdot)\) do likewise. Their choice depends only on the relative weak order, including endpoint equalities, of the four parameters \(0,1,r,x\). There are precisely eleven possible weak-order cases. Representatives are obtained by dividing the following integer pairs \((r,x)\) by \(4\):

```
(0,0) (0,2) (0,4)
(2,0) (2,1) (2,2) (2,3) (2,4)
(4,0) (4,2) (4,4)
```

Every assignment belongs to exactly one of these order types. Gödel operations preserve order-type identifications, so two formulas are equivalent on all real-valued singleton models if and only if their eleven-tuples of values on these representatives agree. Distinct eleven-tuples are therefore genuinely inequivalent formulas. Each coordinate belongs to the finite chain \(\{0,\tfrac14,\tfrac12,\tfrac34,1\}\).

**Step 2: Exhaustive exact algebra certificate.** Regard signatures as eleven-tuples of integers in \(\{0,1,2,3,4\}\), with the common scaling factor \(4\). Define coordinatewise \(\wedge,\vee,\to\), and define \(\Box a\) coordinatewise as \(r\to a\) and \(\Diamond a\) as \(\min(r,a)\). Starting from the signatures of \(\bot,\top,p\), close under the three binary Gödel operations and the permitted unary modality. The supplied `certificate.json` explicitly lists every resulting signature with a derivation: each non-initial entry names its operation and strictly earlier parent indices. The supplied independent `check.py` verifies that every entry has the indicated value, that all signatures are distinct, and that **every** operation applied to **every** appropriate tuple of certified elements again belongs to the certified set.

The exact certified sizes are \(60\) for the box fragment and \(342\) for the diamond fragment. Every listed signature is denoted by its derivation, giving the lower bounds. Closure of the lists under all available connectives, together with containment of the initial signatures, gives the upper bounds by induction on formulas. This is an exhaustive finite proof, not an extrapolation from bounded formula lengths.

**Step 3: A sharp nesting cutoff.** Let \(B_0\) be the propositional closure of the three base signatures. Its six elements are represented by \(\bot,\top,p,\neg p,\neg\neg p,p\vee\neg p\), where \(\neg p:=p\to\bot\). For each permitted modality \(M\), form the propositional closure
\[
 B_1^M=\operatorname{GCl}\bigl(B_0\cup\{Mf:f\in B_0\}\bigr).
\]
A second, separately implemented closure calculation in `check.py` verifies
\[
 |B_0|=6,\quad |B_1^{\Box}|=60,\quad |B_1^{\Diamond}|=342,
\]
and verifies that each \(B_1^M\) is identical to its fully modal-closed certified set. Thus \(B_1^M\) is closed under another modal application: modal depth above one creates no new class. Since both sizes strictly exceed \(6\), depth zero never suffices. For the bimodal fragment, the same cutoff follows from the diamond-only equality proved next.

**Step 4: Modal definability and asymmetry.** On one world, \(\Diamond\top=r\), so for all formulas \(\varphi\),
\[
 \Box\varphi=(\Diamond\top\to\varphi),\qquad
 \Diamond\varphi=(\Diamond\top\wedge\varphi).
\]
Consequently the diamond-only and bimodal languages define exactly the same functions; the box-only language is strictly smaller by the exact counts. In fact, \(\Diamond\top\) cannot be box-only-definable even without counting: when \(x=1\), every box-only formula is \(0\) or \(1\), independently of the intermediate value of \(r\), whereas \(\Diamond\top=r\) can be strictly between them.

## Verification

Place `check.py` and `certificate.json` in the same directory and run `python3 check.py` with a standard Python 3 interpreter; no external Python packages are needed. The checker verifies all \(402\) distinct signatures and their derivation records, all unary applications, all ordered pairs under each propositional binary operation, and an independent depth-one filtration; it prints `GODEL_ONE_WORLD_FRAGMENTS_EXACT_OK 60 342` and both sharp `DEPTH_ONE_NORMAL_FORM` confirmations. The data file is a complete finite witness-and-closure certificate: checking it supplies an exact, finite mathematical proof once the order-type lemma is established. It neither samples arbitrary formulas nor uses a numeric tolerance.

## Relationship to prior work

Ferrari, Fiorentini, Giardini and Rodriguez (2026) develop precisely the witnessed fuzzy Gödel Kripke semantics and establish non-interdefinability of the two modalities over their general model class (Proposition 2.5). Their proof does **not** entail non-interdefinability on singleton frames; here diamond alone actually defines box on that restricted class. Their full paper's semantic definitions and interdefinability section do not state an eleven-case quotient, the \(60\)-element box fragment, or the sharp one-step normal form.

The size \(342\) and the general free-Gödel-algebra counting problem are established classical results, including Horn's 1969 work and Valota's 2019 account. Those results cover the diamond-only/full singleton count once \(r=\Diamond\top\) is observed, but do not directly count the subalgebra obtainable when only \(r\to\cdot\) is available and \(r\) itself cannot be named. The published finite-frame ordinal-regrading theorem shows an order-invariance mechanism and is compatible with Step 1, but counts regrading classes of accessibility matrices rather than term functions or modal fragments. No assertion of novelty is made for the classical free-algebra recurrence or general regrading lemma.

## Limitations

This classification applies only to one world, one propositional letter, Gödel connectives without intermediate truth constants, and numerical equality of truth degrees. It is **not** a collapse of unrestricted Gödel modal logic and does not assert that diamond globally defines box. The numerical \(342\) has classical precedent; the originality question concerns the exact \(60\)-element one-world box subalgebra and its sharp depth filtration. Further historical modal-algebra literature may contain an equivalent calculation, and independent mathematical assessment has not been performed. No count is claimed for two or more worlds or two or more propositional letters.

## References

1. M. Ferrari, C. Fiorentini, P. Giardini and R. O. Rodriguez, “A Gödel Modal Logic Over Witnessed Models,” arXiv:2606.31906, initially public 30 June 2026; *EPTCS* 447 (2026), 355–373. https://arxiv.org/abs/2606.31906
2. D. Valota, “Spectra of Gödel Algebras,” in *Language, Logic, and Computation*, LNCS 11456 (2019), 297–311, DOI:10.1007/978-3-662-59565-7_15. Its general free-spectrum recurrence predates the present specialized fragment calculation.
3. D. Valota, “Computing Spectra of Finite Gödel Algebras through Finite Forests,” TbiLLC 2017 abstract, https://archive.illc.uva.nl/Tbilisi/Tbilisi2017/uploaded_files/inlineitem/Valota.pdf
4. A. Horn, “Free \(L\)-algebras,” *Journal of Symbolic Logic* 34 (1969), 475–480.
5. L. Carai, “Free algebras and coproducts in varieties of Gödel algebras,” *Journal of Symbolic Logic* (2026), DOI:10.1017/jsl.2026.10194.
