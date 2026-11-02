# Independent mathematical audit

## correctness

PASS

For each sparse window, partition sampled indices by residue modulo m. Active start phases sample only binary Sturmian coordinates, with disjoint supports across different phases; their t sampled coordinates have at most 2t patterns from the 2t interval endpoints and can attain 2t by choosing distinct irrational-rotation indices with entrances grouped before exits. Inactive phases each yield one q-letter signature; their exact number is D_c(S). Disjoint alphabets exclude overlaps, giving p*_y(k)=2k+max_{|S|<=k}D_c(S) for every k, including k=1 and k>=m. For |S|=t there are m-t inactive phases and q^t possible words: D<=min(m-t,q^t). Setting s=min{1<=s<=m:q^s>=m-s}, the minima on t<s and t>=s yield min(q^k,m-s). An order-min(k,s) q-ary de Bruijn cycle, repeated across the m-1 decorative positions, realizes all available consecutive t-words. This is an infinite proof; my independently coded exhaustive signature enumerator confirmed all 41 q,m,k triples with q=2,m=2..7 and q=3,m=2..5, not an argument for all cases.

## originality

PASS

The precise all-window invariant and q-ary de Bruijn extremum go beyond the known eventual 2k+C phase-decomposition result, while reusing its acknowledged underlying method. The newer subshift structural theorem does not imply a numerical sharp profile for each periodic decoration. No direct prior coverage was found after Resultary and primary-source comparisons, but a 78-page 2026 thesis remains incompletely accessible and historical priority is qualified.

## value

PASS

The undetermined finite/intermediate-window additive intercept in the natural periodic interleaving family is mathematically meaningful even when eventual affine growth is known. This gives both an exact effective formula for every individual decoration and a sharp alphabet-sensitive extremal capacity formula, with de Bruijn witnesses and clear boundaries. It is not a renaming of eventual linearity: examples with different decorations have different finite profiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
