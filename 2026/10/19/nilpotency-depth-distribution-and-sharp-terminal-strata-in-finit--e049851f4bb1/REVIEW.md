# Independent mathematical audit

## correctness

PASS

Invertible changes of the source and target bases of P give an algebra isomorphism to the rank-r identity sandwich. In that form X^{star j}=X(PX)^{j-1}; the four blocks for j>=2 are A^j, A^{j-1}B, CA^{j-1}, CA^{j-2}B. With A^j=0, H=im A^{j-1} has dimension a and W=ker A^{j-1} has dimension r-a. On a block of size j, A^{j-2}W lands in H; on size j-1 it gives one quotient direction, and on shorter blocks it is zero. Thus B has q^{(r-a-e)b} lifts per map into the e-dimensional quotient image. Once that latter map has rank t, C kills a+t independent directions, and D is free. The usual automorphism-group factor for the Jordan module follows from the endomorphism dimension sum_i (lambda'_i)^2 and semisimple quotient product_s M_{m_s}(F_q). This proves F_j and index-by-differences; j=1 is separate. Nilpotency only tests A; the classical nilpotent count and regular-orbit dimension give the asserted total and irreducible reduced product variety, not scheme reducedness. With two excess sides, the top nonvanishing test uses only CA^{r-1}B and hence regular A; its rank-one factorization gives exactly the two independent nonvanishing factors. The one-side case uses A^{r-1}B or CA^{r-1}, including the direct X test at r=1; no excess sides reduces to the ordinary case. Blocks of each length give indices 1..r, and keeping one or both terminal vectors gives the extra indices when available. Rank zero makes all products zero. Independent replay: python3 /workspace/reproduction.py 2 exhausts ten cases over F_2, F_3 and F_4 with row/column-shifted noncanonical P where possible, computing X(PX)^{j-1} literally. It agrees at every depth and at the terminal stratum, including (q,r,b,c)=(2,3,1,1) with bins (1,575,2912,3360,1344) and (4,1,1,1) with (1,27,36). These tests do not prove the scheme or infinite-parameter claims.

## originality

PASS

Credit the sandwich normal form, ordinary nilpotent counts, and Jordan-orbit sizes as established inputs. The verified rank-one and ordinary square cases are not themselves the basis of originality. The tested strongest comparisons do not provide the arbitrary-rank zero-power strata with both excess dimensions or the general terminal law.

## value

PASS

Knowing the nilpotent locus does not distinguish its power-zero strata. This census identifies the Jordan sizes and quotient rank that govern every depth and explains how the two independent rectangular directions can add zero, one, or two steps to the maximal index. The explicit terminal multiplicity makes that comparison quantitative over every finite field. The value rests on the full depth law rather than on the standard total or rank normal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
