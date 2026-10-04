# Tie-independent Alabama losses for equal-pair rational populations
## Finding
Let the positive primitive integer population vector be \((a,a,c)\) with coprime integers \(a>c>0\), and put \(P=2a+c\). Use Hamilton's largest-remainder rule without imposing an arbitrary tie-break: call a transition tie-independent when both consecutive apportionments are uniquely determined by strict remainder cutoffs.

For a house size \(h\), let \(y\) be the least residue in \(\{0,\ldots,P-1\}\) satisfying
\[
y\equiv ha\pmod P.
\]
A tie-independent Alabama loss occurs from \(h\) to \(h+1\) if and only if
\[
\frac{P+3c}{6}<y<\frac P3.
\]
Whenever this happens, only the state of population \(c\) loses a seat. Since \(\gcd(a,P)=1\), the residues \(y\) run through all residue classes modulo \(P\) as \(h\) runs through one period. Hence the exact number of tie-independent losses per period is
\[
N(a,c)=\max\!\left\{0,\left\lceil\frac P3\right\rceil-
\left\lfloor\frac{P+3c}{6}\right\rfloor-1\right\},
\]
and the corresponding limiting frequency is \(N(a,c)/P\).

The known example \((3,3,1)\) is recovered with \(P=7\), \(N=1\), and loss residue \(h\equiv3\pmod7\). The formula also covers both odd and even \(P\); for example \((7,7,2)\) has \(P=16\) and tie-independent losses at \(h\equiv3,12\pmod{16}\).

## Assumptions and scope
Hamilton's method first assigns each state its lower quota and then distributes the remaining seats to the largest fractional remainders. A unique apportionment means that no tie crosses the cutoff between remainders that receive surplus seats and those that do not. This matters for equal populations because the two \(a\)-states always have equal remainders.

The result concerns exactly three states with two equal larger populations. It counts only losses that do not depend on a lottery or other convention for breaking a cutoff tie. It does not claim a closed formula for arbitrary rational population vectors or for the expected loss rate under a specified random tie-breaking rule.

## Proof
Write the remainder numerators at house size \(h\) as \(y,y,x\), where
\[
y\equiv ha\pmod P,\qquad x\equiv hc\pmod P.
\]
Because \(c=P-2a\),
\[
x\equiv-2y\pmod P.
\]
Also \(\gcd(a,P)=\gcd(a,c)=1\), so multiplication by \(a\) permutes all residues modulo \(P\).

If \(0<y<P/2\), then \(x=P-2y\) and the three remainder numerators sum to \(P\), so exactly one surplus seat is distributed. That seat goes uniquely to the \(c\)-state precisely when
\[
P-2y>y,
\]
equivalently \(y<P/3\). If instead \(P/3\le y<P/2\), the equal \(a\)-states are tied at or above the cutoff, so the apportionment is not uniquely determined.

If \(P/2<y<P\), then \(x=2P-2y\) and the remainder numerators sum to \(2P\), so exactly two surplus seats are distributed. Both \(a\)-states receive them uniquely precisely when
\[
y>2P-2y,
\]
equivalently \(y>2P/3\). For \(P/2<y\le2P/3\), a cutoff tie between the equal \(a\)-states prevents uniqueness. The residue \(y=0\) gives integral quotas, while \(y=P/2\), when it exists, also gives a cutoff tie.

Therefore a tie-independent loss of the small state can occur only when the current residue satisfies \(0<y<P/3\) and the next residue satisfies \(y'>2P/3\). In the first region there is no wrap when adding \(a=(P-c)/2\), because \(y+a<P\), so \(y'=y+a\). Thus
\[
y+a>\frac{2P}{3}
\quad\Longleftrightarrow\quad
y>\frac{P+3c}{6}.
\]
This condition also implies that the lower quota of the \(c\)-state does not increase in the transition: its current remainder numerator is \(P-2y\), and
\[
P-2y+c<P
\]
follows from \(y>(P+3c)/6>c/2\). Hence the loss of its surplus seat is a net loss of one seat.

Conversely, every integer \(y\) in the displayed open interval gives a unique current apportionment with the \(c\)-state rounded up and a unique next apportionment with both \(a\)-states rounded up, while the \(c\)-state's lower quota is unchanged; it therefore gives an Alabama loss. The equal \(a\)-states cannot lose in a unique transition: if they move from the region \(y>2P/3\) to the region \(y'<P/3\), each lower quota rises by one exactly when its surplus-seat indicator drops.

Finally, the integers strictly between \((P+3c)/6\) and \(P/3\) are counted by
\[
\max\!\left\{0,\left\lceil\frac P3\right\rceil-
\left\lfloor\frac{P+3c}{6}\right\rfloor-1\right\}.
\]
Since \(y\equiv ha\pmod P\) is a bijection of residue classes, this count is also the number of house residues producing tie-independent losses.

## Verification
The accompanying verifier implements Hamilton apportionment twice: once with integer quotient/remainder arithmetic and once with exact rational arithmetic. It checks the theorem's residue characterization and count formula for every coprime pair \(a>c>0\) with \(a\le40\), totaling 489 primitive equal-pair cases, and separately checks periodicity. It reproduces the literature anchor \((3,3,1)\) with the single loss residue \(3\bmod7\), as well as even-period examples such as \((7,7,2)\).

The algebraic proof above is the infinite proof; the finite replay is a consistency check rather than an extrapolation.

## Relationship to prior work
Balinski and Young give the standard Hamilton/largest-remainder formulation and the house-monotonicity failure known as the Alabama paradox. Janson and Linusson analyze the probability of the paradox, explicitly note that rational population vectors produce periodic seat-change sequences, and leave exact formulas for general rational vectors open. Their rational examples include \((3/7,3/7,1/7)\), for which the small state loses when the house size moves from \(3\) to \(4\) modulo \(7\).

The present statement does not claim that example as new. It gives a closed formula and exact residue characterization for the entire primitive equal-pair family \((a,a,c)\), restricted to tie-breaking-independent losses. Targeted searches for this equal-pair formula, its interval criterion, and tie-independent terminology did not locate an equivalent published statement.

## Limitations
This theorem does not resolve the full rational-population problem posed by Janson and Linusson. Cutoff-tied house sizes are deliberately excluded rather than assigned a lottery, and arbitrary unequal triples are outside the proved family. Literature search cannot rule out an unindexed note, thesis, or exercise containing an equivalent equal-pair derivation.

## References
1. M. L. Balinski and H. P. Young, “The Quota Method of Apportionment,” *American Mathematical Monthly* 82 (1975), 701–730. DOI: 10.1080/00029890.1975.11993911.
2. S. Janson and S. Linusson, “The probability of the Alabama paradox,” arXiv:1104.2137 (first submitted 2011-04-12); *Journal of Applied Probability* 49 (2012), 773–794. DOI: 10.1239/jap/1346955333.
