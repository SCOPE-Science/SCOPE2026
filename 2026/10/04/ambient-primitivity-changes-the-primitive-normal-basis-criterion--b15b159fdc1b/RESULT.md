# Ambient primitivity changes the primitive-normal-basis criterion for Dickson distributive sets
## Finding
Under Definition 25 of Lee's note, a primitive-normal basis of \(D(1,b)\) over \(\mathbb F_p\) is required to be the complete \(p\)-Frobenius orbit of an element that is primitive in the ambient field \(\mathbb F_{q^n}=\mathbb F_{p^{ln}}\). With that literal definition, such a basis exists exactly when
\[
D(1,b)=\mathbb F_{q^n}.
\]
Thus the implication in Question 26 from \(D(1,b)=\mathbb F_{p^{l\mu}}\) to the existence of the stated primitive-normal basis fails whenever \(\mu<n\) and the smaller field occurs. A concrete failure occurs for the Dickson pair \((q,n)=(4,3)\), where one can have \(D(1,b)=\mathbb F_4\) while the ambient field is \(\mathbb F_{64}\).

If “primitive” in Definition 25 is changed from primitive in \(\mathbb F_{q^n}\) to primitive in \(\mathbb F_{p^{l\mu}}\), then the intended equivalence in Question 26 is true.

## Assumptions and scope
Write \(q=p^l\), let \((q,n)\) be a Dickson pair with \(n>2\), and let \(D(1,b)\subseteq\mathbb F_{q^n}\) be Lee's generalized distributive set, with \(b\) and \(1+b\) nonzero. Let \(s,t\) be the Frobenius-coset parameters from the source and \(\mu=\gcd(s,t,n)\). The source proves \(\mathbb F_{p^{l\mu}}\subseteq D(1,b)\).

The statement here is specifically about Definition 25 as printed: its generating element is required to be a primitive element of the ambient field \(\mathbb F_{q^n}\), where “primitive” means a generator of the nonzero multiplicative group. It does not assert that this was the author's intended wording.

## Proof
Let \(u\in\mathbb F_{p^{ln}}\) be primitive in the ambient field. Then
\[
\operatorname{ord}(u)=p^{ln}-1.
\]
If \(u^{p^d}=u\) for some \(0<d<ln\), then \(u^{p^d-1}=1\), so \(p^{ln}-1\) would divide \(p^d-1\), impossible because \(0<p^d-1<p^{ln}-1\). Hence the orbit of \(u\) under \(z\mapsto z^p\) has exactly \(ln\) distinct elements.

Definition 25 requires a basis consisting of all these algebraic conjugates. Therefore any such basis has \(ln\) elements. Since \(D(1,b)\) is an \(\mathbb F_p\)-subspace of the \(ln\)-dimensional space \(\mathbb F_{p^{ln}}\), the existence of this basis forces
\[
D(1,b)=\mathbb F_{p^{ln}}=\mathbb F_{q^n}.
\]
Conversely, when \(D(1,b)=\mathbb F_{q^n}\), the primitive normal basis theorem gives a primitive element whose full \(p\)-Frobenius orbit is an \(\mathbb F_p\)-basis. This proves the exact criterion under the printed definition.

For an explicit counterexample to the printed implication in Question 26, take \((q,n)=(4,3)\), so \(p=2\) and \(l=2\). Let
\[
\mathbb F_{64}=\mathbb F_2[g]/(g^6+g+1),
\]
where \(g\) has order \(63\), and put \(H=\langle g^3\rangle\). Set
\[
b=g^{34}=g^5+g^2,
\qquad
1+b=g^{31}=g^5+g^2+1.
\]
Because \(34\equiv31\equiv1\pmod 3\), both \(b\) and \(1+b\) lie in \(gH\). Since \(3\mid(4-1)\), this is the Frobenius coset with parameter \(1\), so \(s=t=1\) and \(\mu=1\). In the corresponding Dickson multiplication, left factors in \(gH\) apply the fourth-power Frobenius, whereas \(1\in H\) applies the identity on \(\mathbb F_{64}\). Thus
\[
(1+b)\circ d=1\circ d+b\circ d
\]
is equivalent to
\[
(1+b)d^4=d+bd^4,
\]
and hence to \(d^4=d\). Its solution set is exactly \(\mathbb F_4\). Therefore
\[
D(1,b)=\mathbb F_4=\mathbb F_{p^{l\mu}},
\]
so condition 2 of Question 26 holds, but condition 1 fails: every nonzero element of \(\mathbb F_4\) has order dividing \(3\), while an ambient primitive element of \(\mathbb F_{64}\) has order \(63\).

Finally, if Definition 25 is repaired by replacing “primitive element of \(\mathbb F_{q^n}\)” with “primitive element of \(\mathbb F_{p^{l\mu}}\),” then a full \(p\)-Frobenius orbit has \(l\mu\) elements. If it is a basis of \(D(1,b)\), then \(\dim_{\mathbb F_p}D(1,b)=l\mu\); together with Lee's inclusion \(\mathbb F_{p^{l\mu}}\subseteq D(1,b)\), this forces equality. The converse is precisely the primitive normal basis theorem.

## Verification
The general argument is order-theoretic and does not depend on computation. The accompanying `verify.py` independently performs exact arithmetic in \(\mathbb F_2[g]/(g^6+g+1)\): it verifies that \(g\) has order \(63\), checks \(b=g^{34}\) and \(1+b=g^{31}\) are in the same nontrivial \(H\)-coset, enumerates the Dickson distributivity equation, and confirms that its solution set is exactly the four-element subfield and contains no ambient primitive element.

## Relationship to prior work
Lee's Definition 25 explicitly asks for all algebraic conjugates of a primitive element of the ambient \(\mathbb F_{q^n}\), while Question 26 compares existence of such a basis with the possibly proper subfield \(\mathbb F_{p^{l\mu}}\). The same paper states the primitive normal basis theorem and asserts that condition 2 implies condition 1. The proof above isolates the ambient-versus-subfield mismatch and gives a concrete Dickson-nearfield counterexample.

Djagba's earlier paper develops the same generalized distributive sets and the Dickson multiplication but contains no primitive-normal-basis question. Standard primitive-normal-basis literature uses “primitive” relative to the extension field whose multiplicative group is being generated; applying that theorem to the proper field \(\mathbb F_{p^{l\mu}}\) does not produce an element primitive in the larger ambient field.

## Limitations
The conclusion is a correction to the literal printed definition and question. If the word “primitive” was intended to mean primitive in \(\mathbb F_{p^{l\mu}}\), rather than primitive in the ambient \(\mathbb F_{q^n}\), then the counterexample targets the wording rather than the intended concept; under that repaired definition the equivalence follows as shown above. No claim is made about other notions of normal bases for nonfield generalized distributive sets.

## References
1. K. S. Enoch Lee, “A note on generalized distributive sets of a finite Dickson nearfield,” arXiv:2609.10228v1, 2026.
2. Prudence Djagba, “On the generalized distributive set of a finite nearfield,” arXiv:1903.09695v1; Journal of Algebra 542 (2020), 130–161.
3. H. W. Lenstra Jr. and R. J. Schoof, “Primitive normal bases for finite fields,” Mathematics of Computation 48 (1987), 217–231.
4. Stephen D. Cohen and Sophie Huczynska, “The Primitive Normal Basis Theorem – Without a Computer,” Journal of the London Mathematical Society 67 (2003), 41–56.
