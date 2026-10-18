# Exact dual distributivity spectra in finite Łukasiewicz chains

## Finding

Let \(L_n=\{0,1/n,\ldots,1\}\), where \(n\ge1\), and put \(u\oplus v=\min(1,u+v)\) and \(u\odot v=\max(0,u+v-1)\). Define the two dual distributivity equations

\[
\begin{aligned}
D_\odot(x,y,z):&\quad x\odot(y\oplus z)=(x\odot y)\oplus(x\odot z),\\
D_\oplus(x,y,z):&\quad x\oplus(y\odot z)=(x\oplus y)\odot(x\oplus z).
\end{aligned}
\]

For \(x,y,z\) chosen independently and uniformly from \(L_n\), the numbers of satisfying triples are, exactly,

\[
\boxed{\#D_\odot=\#D_\oplus=\frac{n^3+30n^2+5n+12}{6}},\qquad
\boxed{\#(D_\odot\wedge D_\oplus)=5n^2+n+2}.
\]

In particular, each distributivity equation has limiting satisfaction probability \(1/6\), while the probability that both hold is asymptotic to \(5/n\) and tends to zero. The conditional probability that one holds given the other is asymptotic to \(30/n\).

For an exact description of the simultaneous satisfying locus, use integer coordinates \(a=nx\), \(b=ny\), \(c=nz\). When \(a=0\) or \(a=n\), every \((b,c)\) works. For \(0<a<n\), write \(t=n-a\). Both equations hold precisely in the following cases:

1. \(b=0\) and \(c\ge t\), or \(c=0\) and \(b\ge t\);
2. \(b=n\) and \(c\le t\), or \(c=n\) and \(b\le t\);
3. \(0<b,c<n\) and \(b+c=t\) or \(b+c=2n-a\).

Thus every interior first coordinate has exactly \(3n\) simultaneously satisfying pairs, independent of the first coordinate.

## Assumptions and scope

The objects are the standard finite MV chains \(L_n\) with exactly \(n+1\) truth values, including the Boolean case \(n=1\). Satisfaction of an equation means literal equality of the two evaluated MV terms, not mere attainment of designated truth \(1\) by a separate formula. The three variables are independently and uniformly sampled with replacement. All claims quantify over every integer \(n\ge1\); no restriction to particular parities or asymptotic subsequences is made.

## Proof

**1. Integer normalization.** Multiplying truth values by \(n\) converts the operations to

\[
u\oplus v=\min(n,u+v),\qquad u\odot v=\max(0,u+v-n)
\]

for \(u,v\in\{0,\ldots,n\}\). The following calculations use these scaled operations. If \(a=0\) or \(a=n\), both equations hold for all \((b,c)\), contributing \(2(n+1)^2\) triples to either equation and to their conjunction. These are distinct first-coordinate layers because \(n\ge1\).

**2. Count the first law.** Fix \(0<a<n\), set \(t=n-a\) (so \(1\le t<n\)), and partition the \((b,c)\)-square into the four regions given by comparison with \(t\).

If \(b,c\le t\), the right-hand side of \(D_\odot\) is zero; the left-hand side is \(\min(a,\max(0,b+c-t))\). Hence equality holds precisely for \(b+c\le t\), giving \(\binom{t+2}{2}\) pairs.

If \(b>t\) and \(c\le t\), the right-hand side is \(b-t\), whereas the left-hand side is \(\min(a,b+c-t)\). Since \(b-t>0\), equality holds precisely when \(c=0\) or \(b=n\). There are \(a\) pairs of the first kind and \(t\) additional pairs of the second kind, for \(a+t=n\) in this region. The symmetric region \(c>t\), \(b\le t\) contributes another \(n\) pairs.

If \(b,c>t\), the left-hand side is \(\min(a,b+c-t)\), and the right-hand side is \(\min(n,b+c-2t)\). Because \(0<t\) and \(a<n\), any equality must occur when the first expression equals its cap \(a\) and the second expression equals the same \(a\), which is equivalent to \(b+c=a+2t=2n-a\). There are exactly \(a-1\) such pairs: \(b\) can range from \(t+1\) through \(n-1\), and \(c\) is then forced.

Thus for the fixed interior first coordinate the count is

\[
\binom{t+2}{2}+2n+(a-1)=\binom{t+2}{2}+3n-t-1.
\]

Summing over \(t=1,\ldots,n-1\) and adding the two endpoint layers yields

\[
\begin{aligned}
\#D_\odot
&=2(n+1)^2+\sum_{t=1}^{n-1}\left[\binom{t+2}{2}+3n-t-1\right]\\
&=2(n+1)^2+\binom{n+2}{3}-1+\frac{(n-1)(5n-2)}{2}\\
&=\frac{n^3+30n^2+5n+12}{6}.
\end{aligned}
\]

The formula remains valid for \(n=1\), when the sum is empty and \(\binom{3}{3}-1=0\).

**3. Duality.** The involution \(u\mapsto n-u\) exchanges \(\oplus\) with \(\odot\) by the MV De Morgan laws. The bijection \((a,b,c)\mapsto(n-a,n-b,n-c)\) therefore maps satisfying triples for \(D_\odot\) to satisfying triples for \(D_\oplus\), proving equality of their counts.

**4. Simultaneous locus and count.** Fix \(0<a<n\) and \(t=n-a\). On the boundary \(b=0\), the first law holds automatically and the second is equivalent to \(c\ge t\); on \(b=n\), the second holds automatically and the first is equivalent to \(c\le t\). Interchanging \(b,c\) gives the other two boundary segments in the stated classification. Their combined size is \(2(a+1)+2(t+1)-2=2n+2\), subtracting the two twice-counted corners \((b,c)=(0,n),(n,0)\).

For \(0<b,c<n\), Step 2 implies that the first law holds only if (i) \(b,c\le t\) and \(b+c\le t\), or (ii) \(b,c>t\) and \(b+c=2n-a\). Applying Step 2 to the complemented triple shows that the dual law holds only if (i') \(b,c<t\) and \(b+c=t\), or (ii') \(b,c\ge t\) and \(b+c\ge2n-a\). Their intersection consists precisely of \(b+c=t\) or \(b+c=2n-a\), with \(b,c\) strictly interior. The first diagonal has \(t-1\) such pairs, the second has \(a-1\), and they are disjoint. Thus the interior part contributes \(t-1+a-1=n-2\). Combined with the boundary contribution, there are exactly \(3n\) pairs for each \(a\in\{1,\ldots,n-1\}\).

Therefore the simultaneous count is

\[
2(n+1)^2+(n-1)3n=5n^2+n+2.
\]

**5. Asymptotics.** All \((n+1)^3\) ordered assignments are equally likely. Dividing the exact counts by this denominator gives \(\Pr(D_\odot)=\Pr(D_\oplus)\to1/6\) and \(\Pr(D_\odot\wedge D_\oplus)=5/n+O(n^{-2})\). Their quotient gives \(\Pr(D_\oplus\mid D_\odot)=30/n+O(n^{-2})\).

## Verification

The included `verify.py` evaluates both original MV-term equations directly using integer minima and maxima, independently tests the derived region classifications for each assignment, and compares the resulting counts with the closed formulas. Executing `python3 verify.py` checked every triple for denominators \(1\) through \(45\), in total \(1{,}168{,}560\) triples, with no discrepancy. These finite tests are independent checks of the boundary handling and algebra, not substitutes for the proof for arbitrary \(n\).

## Relationship to prior work

Bofill, Manyà, Vidal, and Villaret (2018, Section 4) explicitly note that the Łukasiewicz strong conjunction does not distribute over strong disjunction. Their main results concern satisfiability complexity and translations; the inspected article does not provide the satisfaction counts, exact simultaneous-locus description, or opposite asymptotic behaviors above. The De Morgan duality used in Step 3 is standard and is not claimed as new.

Preto and Finger (2022) develop representations of continuous piecewise-linear functions in Łukasiewicz logic. That work provides relevant expressiveness context, but the available abstract does not settle whether its inaccessible full text contains a related quantitative calculation. The exact counts here also do not follow from a mere observation that distributivity fails: they require classifying all satisfying triples. Previously known polyhedral and finite-grid counting machinery could potentially yield these coefficients, and the provenance of this particular evaluation should receive an independent literature check before a priority claim.

## Limitations

The result applies to the two specified strong-connective equations on standard finite Łukasiewicz chains only, with uniform independent assignments. It does not classify all distributive-type equations, nonchain MV-algebras, product or Gödel t-norms, or arbitrary sampling distributions. Priority relative to inaccessible full-text literature has not been independently established.

## References

1. M. Bofill, F. Manyà, A. Vidal, and M. Villaret, *New complexity results for Łukasiewicz logic*, Soft Computing 23 (2019), 2187–2197. First published online 11 July 2018. DOI: https://doi.org/10.1007/s00500-018-3365-9.
2. S. Preto and M. Finger, *Efficient representation of piecewise linear functions into Łukasiewicz logic modulo satisfiability*, Mathematical Structures in Computer Science 32 (2022), 1119–1144. DOI: https://doi.org/10.1017/S096012952200010X.
